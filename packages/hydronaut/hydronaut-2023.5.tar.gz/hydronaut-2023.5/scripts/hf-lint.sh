#!/usr/bin/env bash
set -euo pipefail

SELF=$(readlink -f "${BASH_SOURCE[0]}")
source "${SELF%/*/*}/env.sh"

"$HYDRONAUT_DIR/submodules/utility-scripts/scripts/pylint.sh" \
  "$HYDRONAUT_DIR/src" \
  "$HYDRONAUT_DIR/examples"/*/src
