#!/bin/bash -i
set -e
set -o pipefail

# install pylint
echo "installing pylint..."
sudo apt install pylint

# install pre-commit
echo "installing pre-commit..."
sudo apt install pre-commit
pre-commit install

# install Python requirements
echo "installing python requirements..."
pip3 install -r requirements.txt --upgrade --upgrade-strategy eager

# apply changes to shell
echo "installation finished! 🔥"
echo "restarting shell..."
exec "$SHELL"
