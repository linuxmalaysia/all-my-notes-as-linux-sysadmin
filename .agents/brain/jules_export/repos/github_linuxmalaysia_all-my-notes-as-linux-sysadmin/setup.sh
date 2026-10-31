#!/usr/bin/env bash
set -euo pipefail
# Jules setup script for all-my-notes-as-linux-sysadmin
npm install
uv run --with pytest --with pyyaml --with pytest-cov --with defusedxml python run_all_tests.py
