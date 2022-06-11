#!/bin/bash -i
set -e
set -o pipefail

# setup pyenv
echo "installing pyenv..."
brew install pyenv

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# install pre-commit
echo "installing pre-commit..."
brew install pre-commit
pre-commit install

# install Python requirements
echo "installing python requirements..."
pip3 install -r requirements.txt --upgrade --upgrade-strategy eager

# apply changes to shell
echo "installation finished! 🔥"
echo "restarting shell..."
exec "$SHELL"
