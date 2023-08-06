#!/usr/bin/env python3
'''
MLflow utility functions.
'''

import logging
import os
from contextlib import ExitStack
from types import TracebackType
from typing import Any, Optional, Type

import mlflow
from hydra.core.hydra_config import HydraConfig
from hydra.utils import to_absolute_path
from omegaconf import DictConfig, ListConfig

from hydronaut.hydra.omegaconf import get, get_container


LOGGER = logging.getLogger(__name__)


def _recursively_log_omegaconf_params_with_mlflow(name: str, obj: Any) -> None:
    '''
    Recursively log the Hydra parameters.

    Args:
        name:
            The parameter name.

        obj:
            The parameter object.
    '''
    if isinstance(obj, DictConfig):
        for key, value in obj.items():
            _recursively_log_omegaconf_params_with_mlflow(f'{name}.{key}', value)
    elif isinstance(obj, ListConfig):
        for i, value in enumerate(obj):
            _recursively_log_omegaconf_params_with_mlflow(f'{name}.{i:d}', value)
    else:
        LOGGER.debug('logging parameter: %s = %s', name, obj)
        mlflow.log_param(name, obj)


class MLflowRunner():
    '''
    Context manager to set up an MLflow run from an Omegaconf configuration
    object. When used as a context manager, it will configure the tracking URI,
    experiment, artifact location and run parameters from the configurat object.
    The context will return the MLflow active run.
    '''
    def __init__(self, config: DictConfig) -> None:
        '''
        Args:
            config:
                The Omegaconf configuration object.
        '''
        self.config = config
        self.exit_stack = ExitStack()

    def log_parameters(self) -> None:
        '''
        Log all parameters with MLflow.
        '''
        for name, value in self.config.items():
            _recursively_log_omegaconf_params_with_mlflow(name, value)

    def _set_experiment(self) -> mlflow.entities.Experiment:
        '''
        Set the current experiment from the name in the configuration object.

        Returns:
            An instance of mlflow.entities.Experiment.
        '''
        config = self.config

        exp_name = config.experiment.name
        LOGGER.info('MLflow experiment name: %s', exp_name)

        exp = mlflow.get_experiment_by_name(exp_name)
        if exp is None:
            exp_id = mlflow.create_experiment(name=exp_name)
            exp = mlflow.get_experiment(exp_id)
        mlflow.set_experiment(experiment_id=exp.experiment_id)

        return exp

    def _set_uris(self) -> None:
        '''
        Log and set the MLflow URIs.
        '''
        tracking_uri = mlflow.get_tracking_uri()
        LOGGER.info('MLflow tracking URI: %s', tracking_uri)

        registry_uri = os.getenv('MLFLOW_REGISTRY_URI', default=tracking_uri)
        if registry_uri:
            mlflow.set_registry_uri(registry_uri)

        LOGGER.info(
            'MLflow registry URI: %s',
            mlflow.get_registry_uri()
        )

    def __enter__(self) -> mlflow.ActiveRun:
        config = self.config
        hydra_config = HydraConfig.get()

        stack = self.exit_stack
        self._set_uris()
        self._set_experiment()

        run_kwargs = get_container(self.config, 'experiment.mlflow.start_run', default={})

        run_name = config.experiment.name
        job_id = hydra_config.job.get('id')
        if job_id:
            run_name = f'{run_name}-{job_id}'
        run_kwargs['run_name'] = run_name

        for key, value in sorted(run_kwargs.items()):
            LOGGER.debug('MLflow start_run parameter: %s = %s', key, value)

        active_run = stack.enter_context(mlflow.start_run(**run_kwargs))

        LOGGER.info(
            'MLflow artifact URI: %s',
            mlflow.get_artifact_uri()
        )

        self.log_parameters()
        return active_run

    def __exit__(
        self,
        typ: Optional[Type[BaseException]],
        value: Optional[BaseException],
        traceback: Optional[TracebackType]
    ) -> bool:
        self.exit_stack.close()
