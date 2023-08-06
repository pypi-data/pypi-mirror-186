#!/usr/bin/env bash

HYDRONAUT_ENV_FILE=$(readlink -f "${BASH_SOURCE[0]}")
HYDRONAUT_DIR=${HYDRONAUT_ENV_FILE%/*}
HYDRONAUT_DEFAULT_VENV_DIR=$HYDRONAUT_DIR/venv

source "$HYDRONAUT_DIR/submodules/utility-scripts/sh/prepend_to_paths.sh"
prepend_to_PATH "$HYDRONAUT_DIR/submodules/utility-scripts/scripts"
prepend_to_PATH "$HYDRONAUT_DIR/scripts"
