#!/bin/bash -i
set -e
set -o pipefail

# setup pyenv
echo "installing pyenv..."
brew install pyenv

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# apply changes to shell
echo "installation finished! 🔥"
echo "restarting shell..."
exec "$SHELL"
