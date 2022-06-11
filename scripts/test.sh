#!/bin/bash
set -e
set -o pipefail

# lint
mypy
pylint -j0 -E ../**/*.py

# run tests
echo "running tests..."
pytest