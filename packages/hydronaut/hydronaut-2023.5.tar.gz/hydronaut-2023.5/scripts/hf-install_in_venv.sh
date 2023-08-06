#!/usr/bin/env bash
set -euo pipefail

SELF=$(readlink -f "${BASH_SOURCE[0]}")
source "${SELF%/*/*}/env.sh"

cd "$HYDRONAUT_DIR"
cmd=(
  "submodules/utility-scripts/scripts/pip-install_in_venv.sh"
  "$@"
  "$HYDRONAUT_DIR"
)
echo "${cmd[*]@Q}"
"${cmd[@]}"
