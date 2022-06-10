<img src="https://user-images.githubusercontent.com/55748056/172958283-fa9b17c3-16a5-49e7-9a12-3d33dc5b6f6d.png" width="300">
    
Dory
====

Dory is a **Python3.7+** out-of-the box smart cache library.   
It simplifies multiple cache features and brings [Bloats](#Bloats) to the table, a tool designed to make smarter your application cache.

&nbsp; | Badges
--- | ---
Build | [![tests](https://github.com/sorenrife/dory/actions/workflows/test.yaml/badge.svg?branch=master&event=push)](https://github.com/sorenrife/dory/actions/workflows/test.yaml) [![build/deploy](https://github.com/sorenrife/dory/actions/workflows/deploy-prod.yaml/badge.svg)](https://github.com/sorenrife/dory/actions/workflows/deploy-prod.yaml) [![codecov](https://codecov.io/gh/sorenrife/dory/branch/master/graph/badge.svg?token=72DJGGO049)](https://codecov.io/gh/sorenrife/dory)
Docs | [![documentation](https://img.shields.io/badge/dory-docs-FF274D)](https://sorenrife.gitbook.io/dory/)
Package | [![PyPi](https://img.shields.io/pypi/v/dory-cache.svg)](https://pypi.python.org/pypi/dory-cache/) [![PyPi versions](https://img.shields.io/pypi/pyversions/dory-cache.svg)](https://pypi.python.org/pypi/dory-cache/) [![code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
Support | [![discord](https://img.shields.io/discord/923086216704974889?logo=discord)](https://discord.com/channels/923086216704974889/926482337858998292)

## Table of content

- [Installation](#Installation)
- [Features](#Features)
    - [Cache utils](#Cache-utils)
    - [Bloats](#Bloats)
- [Usage](#Usage)
    - [Examples](#Examples)
- [Roadmap](#Roadmap)
- [Contributing](#Contributing)

## Installation

Installation is as simple as:

```bash
pip install dory-cache
```

## Features

### Cache utils

Dory implements several cache utilities with a simple interface. For example, a decorator to cache views comfortably:

```python
@blueprint.get('/foo')
@dory.cache(key='foo', timeout=timedelta(hours=1))
def foo(request):
    """
    Render a Foo
    """
    ...

```

More about on the [docs](https://sorenrife.gitbook.io/dory/) 🔥

## Roadmap

- [ ] Cache utils
- [ ] Bloats 🐡
- [ ] Django signals
- [ ] Ratelimit
- [ ] Bloats v2

## Contributing

Suggestions and contributions are extremely welcome! ❤️  
Just open an issue or a PR, and we'll respond as soon as we can.
