---
title: README
author: Jan-Michael Rye
---

![Hydronaut logo](https://gitlab.inria.fr/jrye/hydronaut/-/raw/main/img/hydronaut_logo.svg)

# Synopsis

Hydronaut is a framework for exploring the depths of hyperparameter space with [Hydra](https://hydra.cc/docs/intro/) and [MLflow](https://mlflow.org/). Its goal is to encourage and facilitate the use of these tools while handling the sometimes unexpected complexity of using them together. Users benefit from both without having to worry about the implementation and are thus able to focus on developing their models.

Hydra allows the user to organize all hyperparameters via simple YAML files with support for runtime overrides via the command-line. It also allows the user to explore the hyperparameter space with automatic sweeps that are easily parallelized. These sweeps can either explore all possible parameter combinations or they can use any of the [optimizing sweepers supported by Hydra](https://hydra.cc/docs/intro/) such as the [Optuna Sweeper plugin](https://hydra.cc/docs/plugins/optuna_sweeper/). The hyperparameters used for every run are automatically saved for future reference.

MLflow is a platform for tracking experiments and their results, among other things. The library provides numerous [logging functions](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.log_artifact) to track hyperparameters, metrics, artifacts and models of every run so that nothing is ever lost or forgotten. The results can be readily perused, compared and managed via a web interface that can be launched with the command `mlflow ui` in the output directory. It can also be used to push trained models to registries.

# Installation

Install the [Hydronaut package](https://pypi.org/project/hydronaut) from the [Python Package Index](https://pypi.org/) using any standard Python package manager, e.g.

~~~sh
# Uncomment the following 2 lines to create and activate a virtual environment.
# python -m venv venv
# source venv/bin/activate
pip3 install --upgrade hydronaut
~~~

It can also be installed from source with any standard Python package manager that supports [pyproject.toml](https://peps.python.org/pep-0621/) files. For example, to install it with pip, either locally or in a virtual environment, run the following commands:

~~~sh
git clone --recursive https://gitlab.inria.fr/jrye/hydronaut
cd hydronaut
# Uncomment the following 2 lines to create and activate a virtual environment.
# python -m venv venv
# source venv/bin/activate
pip install --upgrade .
~~~

Note that the Hydronaut Git repository contains Git submodules. It should be recursively cloned with `git clone --recursive https://gitlab.inria.fr/jrye/hydronaut` to check out all requirements. Alternatively, after cloning the repository non-recursively one can run `git submodule update --init --recursive` to fully initialize the repository. This can also be accomplished with the script [hf-initialize.sh](https://gitlab.inria.fr/jrye/hydronaut/-/blob/main/scripts/hf-initialize.sh), which is provided for convenience.

The project also provides the script [hf-install_in_venv.sh](https://gitlab.inria.fr/jrye/hydronaut/-/blob/main/scripts/hf-install_in_venv.sh) which can be used to install the package in a virtual environment. Internally, the script uses `pip-install.sh` from the utility-scripts submodule which can circumvent a bug in the way that`hatch-vcs` handles Git submodules.

## Submodules

* [utility-scripts](https://gitlab.inria.fr/jrye/utility-scripts)


# Usage

There are only two requirements for running an experiment with Hydronaut:

* A Hydra YAML configuration file located at `conf/config.yaml` relative to the current working directory.
* A subclass of the Hydronaut `Experiment` class, which is defined in [hydronaut.experiment](https://gitlab.inria.fr/jrye/hydronaut/-/blob/main/src/hydronaut/experiment.py).

A different configuration file can be specified by setting the `HYDRONAUT_CONFIG` environment variable. The value of this variable will be interpreted as a subpath within the `conf` directory of the working directory.

The `Experiment` subclass is specified via the configuration file's `experiment.exp_class` field as a string with the format `<module>:<class>` where `<module>` is the Python module containing the subclass and `<class>` is its name. Uninstalled Python modules and packages can be made importable by adding their containing directories to the `experiment.python.paths` list in the configuration file. See the [dummy example](https://gitlab.inria.fr/jrye/hydronaut/-/tree/main/examples/dummy) for an example of a simple configuration file and `Experiment` subclass with only one module.

Once the configuration file and `Experiment` subclass have been created, the experiment can be run with `hf-run` or `hf-run_in_venv.sh` (see below).



## API Documentation

The [Sphinx](https://www.sphinx-doc.org/en/master/)-generated online API documentation is available here: <https://jrye.gitlabpages.inria.fr/hydronaut/>



## Hydra Configuration File

Hydronaut used [Hydra](https://hydra.cc/), which in turn uses [OmegaConf](https://github.com/omry/omegaconf) configuration files. The [Hydra start guide](https://hydra.cc/docs/intro/) provides a good and quick introduction to the functionality provided by Hydra.

The basic idea is that you should set all of your experiment's parameters in the configuration file and then retrieve them from the configuration object in your code. This will grant the following advantages:

* All parameters can be modified in one place without changing the code.
* All parameters can be overridden from the command line.
* The effects of different parameters and parameter combinations can be explored automatically using Hydra's sweeper plugins.
* The exact parameters used for each run are stored automatically in structured output files along with all artifacts and metrics that your experiment creates.
* Only a single object needs to be passed around in your code instead of an ever-changing list of parameters.

In addition to the reserved Hydra fields (`hydra`, `defaults`), Hydronaut add an `experiment` field with some required values:

~~~yaml
experiment:
  name: <experiment name>                # required
  description: <experiment description>  # required
  exp_class: <module>:<class>            # required
  params: <experiment parameters>
  python:
    paths: <list of directories to add to the Python system path>
  mlflow: <MLflow configuration>
~~~

It is strongly recommended that all experiment parameters be nested under `experiment.params` but this is not enforced programmatically unless the `hf_config` or `experiment/hf_experiment` default is used.

The best way to get started is to take a look at the configuration files in the provided [examples](https://gitlab.inria.fr/jrye/hydronaut/-/tree/main/examples). `hf-init` can also be used to initialize a directory for a new experiment.

For more details, consult the [Hydra](https://hydra.cc/docs/intro/) and [OmegaConf](https://omegaconf.readthedocs.io/en/) documentation, e.g.

* [command-line flags](https://hydra.cc/docs/advanced/hydra-command-line-flags/)
* [defaults list](https://hydra.cc/docs/advanced/defaults_list/)
* [extending configs](https://hydra.cc/docs/patterns/extending_configs/)
* [override syntax](https://hydra.cc/docs/advanced/override_grammar/basic/)
* [tab completion](https://hydra.cc/docs/tutorials/basic/running_your_app/tab_completion/)
* [variable interpolation](https://omegaconf.readthedocs.io/en/latest/usage.html#variable-interpolation)


### Resolvers

Resolvers are functions that can be used to insert values into fields of the configuration file, such as the current date (`${now:%Y-%m-%d}`) or the number of available CPU cores (`${n_cpu:}`). Hydronaut provides some custom resolvers in addition to the ones provided by [OmegaConf](https://omegaconf.readthedocs.io/en/latest/custom_resolvers.html#built-in-resolvers) and [Hydra](https://hydra.cc/docs/configure_hydra/intro/#resolvers-provided-by-hydra). See [hydronaut.hydra.resolvers](https://gitlab.inria.fr/jrye/hydronaut/-/blob/main/src/hydronaut/hydra/resolvers.py) for details.



## Examples

Examples of varying complexity are provided in the [examples directory](https://gitlab.inria.fr/jrye/hydronaut/-/tree/main/examples). The [dummy example](https://gitlab.inria.fr/jrye/hydronaut/-/blob/main/examples/dummy/README.md) provides the simplest albeit least interesting example of a minimal setup. Peruse the others to get an idea of how to create more interesting experiments.



## Commands

The following commands are installed with the Python package.


### hf-run

Run `hf-run` (equivalent to `python -m hydronaut.run`) in the working directory to load the configuration file and run the experiment. After the script has started, run `mlflow ui` in the same directory and then open the URL that it shows in a web browser. All of the experiments results will appear under the name given to the experiment in the configuration file.

`hf-run` accepts all of [Hydra's command-line flags](https://hydra.cc/docs/advanced/hydra-command-line-flags/). For example, to show Hydra information, run `hf-run --info`.

~~~sh
# Usage:
hf-run [<hydra arguments>]

# For example:
hf-run --cfg job
hf-run --multirun experiment.params.foo=42
~~~



### hf-init

Hydronaut also provides a script named `hf-init` which will generate a commented configuration file and an Experiment subclass skeleton under the current working directory which can be used as a starting point for a new experiment.

See `hf-init --help` for available options.


## Scripts

The following convenience scripts are provided in the source repository for common operations.

### hf-initialize.sh

[hf-initialize.sh](https://gitlab.inria.fr/jrye/hydronaut/-/blob/main/scripts/hf-initialize.sh) is just a convenience script for recursively checking out the submodules. It may be extended later.

~~~sh
# Usage:
hf-initialize.sh
~~~



### hf-install_in_venv.sh

[hf-install_in_venv.sh](https://gitlab.inria.fr/jrye/hydronaut/-/blob/main/scripts/hf-install_in_venv.sh) will install Hydronaut in a virtual environment. If the virtual environment does not exist then it will be created.

See `hf-install_in_venv.sh -h` for details.




### hf-lint.sh

[hf-lint.sh](https://gitlab.inria.fr/jrye/hydronaut/-/blob/main/scripts/hf-lint.sh) will report warnings and errors in the Hydronaut source files and examples.

~~~sh
# Usage:
hf-lint.sh
~~~



### hf-rsync-results.sh

[hf-rsync-results.sh](https://gitlab.inria.fr/jrye/hydronaut/-/blob/main/scripts/hf-rsync-results.sh) will transfer files that result from an experiment in the source directory to a destination using rsync. It can be used to retrieve results from a cluster, for example.

~~~sh
# Usage:
hf-rsync-results.sh [<rsync options>] <rsync destination>
~~~



### hf-run_in_venv.sh

[hf-run_in_venv.sh](https://gitlab.inria.fr/jrye/hydronaut/-/blob/main/scripts/hf-run_in_venv.sh) is a wrapper around `hf-run` that will first set up a virtual environment and install Hydronaut before running `hf-run` in the current directory. If the current directory contains a `pyproject.toml` or `requirements.txt` file, they will also be installed in the virtual environment before running `hf-run`.

See `hf-run_in_venv.sh -h` for details.


## MLflow

Hydronaut only uses a fraction of the full functionality of MLflow. For example, beyond tracking your experiments, it can also be used to package and distribute your code via standard platforms to facilitate collaboration with others. The interested user should consult the [MLflow documentation](https://mlflow.org/docs/latest/index.html) to get an idea of what is possible.

Most of the MLflow functionality is available via the [command-line interface](https://mlflow.org/docs/latest/cli.html) (`mlflow`). For additional functionality the user may also be interested in [MLflow Extra](https://gitlab.inria.fr/jrye/mlflow-extra).

### Useful Examples

~~~sh
# Find an experiment ID.
mlflow experiment list

# Export all of its parameters and metrics to a CSV file
mlflow experiment csv -x <ID>
~~~


# Troubleshooting

## Hydra Configuration In Subprocesses

Due to limitations in Hydra's support for subprocesses, it is usually necessary to re-initialize the Hydra configuration in subprocesses such as PyTorch DataLoaders running as separate workers. Hydronaut provides the [configure_hydra](https://jrye.gitlabpages.inria.fr/hydronaut/hydronaut.hydra.html?highlight=configure_hydra#hydronaut.hydra.config.configure_hydra) function to facilitate this.

~~~python
from hydronaut.hydra.config import configure_hydra
# ...
configure_hydra(from_env=True)
~~~

The configuration uses environment variables that are set during initialization of the [Experiment](https://jrye.gitlabpages.inria.fr/hydronaut/hydronaut.html?highlight=experiment#hydronaut.experiment.Experiment) base class.

## CUDA/NVCC Errors With PyTorch

Check that the version of PyTorch is compatible with the one installed on the system:

~~~sh
# System CUDA version
nvcc -V

# PyTorch CUDA version
python -c 'import torch; print(torch.version.cuda)'
~~~

If the versions are mismatched, consult the [PyTorch Start Locally guide](https://pytorch.org/get-started/locally/) for commands to install a compatible version in a virtual environment. If PyTorch is already installed in the current (virtual) environment, append `--upgrade` to the install command (e.g. `pip install --upgrade ...`).

## Hydra Joblib Launcher Plugin And PyTorch DataLoader Threads

The [Hydra Joblib Launcher plugin](https://hydra.cc/docs/plugins/joblib_launcher/) is currently not compatible with [PyTorch DataLoader worker processes](https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader). Either disable the Joblib launcher or set the number of worker processes to 0 when instantiating DataLoaders (`num_workers=0`).


# Further Reading

## Optuna

* [Optuna website](https://optuna.org/)
* [Hydra Optuna Sweeper plugin documentation](https://hydra.cc/docs/plugins/optuna_sweeper/)
* [Multi-objective Optimization with Optuna](https://hydra.cc/docs/plugins/optuna_sweeper/#example-2--multi-objective-optimization)

## PyTorch Lighting

* [Introduction](https://towardsdatascience.com/from-pytorch-to-pytorch-lightning-a-gentle-introduction-b371b7caaf09)
* [Callbacks](https://pytorch-lightning.readthedocs.io/en/stable/extensions/callbacks.html)
