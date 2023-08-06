---
title: TODO
---

# Hydronaut Package

* Determine how to support interruptable experiments with automatic resumption.
* Provide methods for storing and logging artifacts.
* Maybe provide utility functions for generating common artifacts such as confusion matrices and learning curves. These should be library-agnostic.
* Determine how to expose output file path configuration options via the configuration file. In particular, check how to collate results from different working directories in a common MLflow session.

# Examples

* Create a simplified version of the current MNIST example (e.g. 3 fully connected layers) and use that as a base class for the current convolution model.
* Rename the MNIST example to clarify that it uses PyTorch Lightning and create an equivalent PyTorch experiment without PyTorch Lightning.
* Create an sklearn example.

# Meta

* Facilitate CUDA version matching via the installation script to ensure e.g. that PyTorch is compatible with the installed version of CUDA (`nvcc -V`).
* Explain Experiment class and usage (via Sphinx documentation?).
* Maybe add helper utility for launching `mlflow ui`.

# Unit Tests

Decide on a strategy for unit testing and then implement the tests.
