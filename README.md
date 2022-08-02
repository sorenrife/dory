<img src="https://user-images.githubusercontent.com/55748056/172958283-fa9b17c3-16a5-49e7-9a12-3d33dc5b6f6d.png" width="300">
    
Dory
====

Dory is a **Python3.8+** out-of-the box smart cache solution. It simplifies multiple cache features and brings [Bloats](#Bloats) to the table, a tool designed to make smarter your application cache.

&nbsp; | Badges
--- | ---
Build | [![tests](https://github.com/sorenrife/dory/actions/workflows/test.yaml/badge.svg?branch=master&event=push)](https://github.com/sorenrife/dory/actions/workflows/test.yaml) [![build/deploy](https://github.com/sorenrife/dory/actions/workflows/deploy.yaml/badge.svg)](https://github.com/sorenrife/dory/actions/workflows/deploy.yaml) [![codecov](https://codecov.io/gh/sorenrife/dory/branch/master/graph/badge.svg?token=72DJGGO049)](https://codecov.io/gh/sorenrife/dory)
Docs | [![documentation](https://img.shields.io/badge/dory-docs-FF274D)](https://sorenrife.gitbook.io/dory/)
Package | [![PyPi](https://img.shields.io/pypi/v/dory-cache.svg?color=blue)](https://pypi.python.org/pypi/dory-cache/) [![PyPi versions](https://img.shields.io/pypi/pyversions/dory-cache.svg?color=blue)](https://pypi.python.org/pypi/dory-cache/) [![code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
Support | [![buy-me-a-coffee](https://img.shields.io/badge/-buy_me_a%C2%A0coffee-gray?logo=buy-me-a-coffee)](https://www.buymeacoffee.com/sorenrife)

## Table of content

- [Installation](#Installation)
- [Features](#Features)
    - [Bloats](#Bloats)
    - [Cache utils](#Cache-utils)
- [Usage](#Usage)
    - [Examples](#Examples)
- [Roadmap](#Roadmap)
- [Contributing](#Contributing)

## Installation

Installation is as simple as:

```bash
pip install dory-cache
```

View the current documentation [here](https://sorenrife.gitbook.io/dory/).

## Features

### Bloats
<p align="center">
    <img src="https://user-images.githubusercontent.com/55748056/173080628-aafb7b87-67c4-4181-9619-01ee7a4126bc.png" width="300">
</p>
<p align="center"><i>Porcupinefish have the ability to inflate their bodies by swallowing water or air, thereby becoming rounder.</i></p>
<br>

`Bloats` responds to the necessity to have a solid and clean way to define cache usage and to permit an smart cache approach to your system.
The main idea behind it is that a `Bloat` has the ability to `inflate` -as a *Porcupinefish* does- meaning that has the ability to cache a `key/value` given a certain configuration and return the stored value -or return it directly if it was already cached-.
Also, has the ability to `deflate` meaning exactly the contrary, that deletes the given `key/value` from the cache. Having a `Bloat` decoupled gives the application the ability to interact with the cache in a comfortable way around all the project.


For example, let's pretend that we have a model called `Product` wich can be either renderizer or edited. So, to improve the `Product` serialization performance we cache the `Product` serialization view **(GET /product/<id>)**.

```python
from dory import cache
from dory.utils import F

@api.get('/product/<product_id>')
@cache.get(key="product:%s" % F('product_id'), timeout=timedelta(hours=1))
def get_product(request, product_id) -> Response:
    """
    Serialize a Product
    """
    ...
```

Now everything works faster and as expected, but we did not contemplate that since the `Product` can be edited **(PUT /product/<id>)**, we could have cached an outdated version of the `Product`, so we need a way to force the cache to refresh itself. This is where **Bloats** come in handy!

Instead of caching the view with a generic cache decorator, decouple the cache configuration on a `Bloat`:

```python
from dory import bloats

class Product(bloats.Bloat):
    """
    Product's bloat
    """
    prefix: str = 'product'
    key: str
    
    timeout: timedelta = timedelta(hours=1)
    enabled: bool = True
    
    def __init__(product_id: int):
        self.key = '%s' % product_id
```

```python
from dory import cache
from dory.utils import F

@api.get('/product/<product_id>')
@bloats.Product.get(product_id=F('product_id'))
def get_product(request, product_id) -> Response:
    """
    Serialize a Product
    """
    ...
```

And now, when a `Product` is edited, you can force the view to refresh the cache using the `Bloat` as a middle-man.

```python
@api.put('/product/<product_id>')
@bloats.Product.touch(product_id=F('product_id'))
def edit_product(request, product_id):
    """
    Edit a Product
    """
    ...
```

Now your cache will always be in sync and it'll be configured in a cleaner way! 🔥

### Cache utils

**Dory** simplifies several cache utilities with an out-of-the-box interface. For example, a decorator to cache views comfortably:

```python
@api.get('/foo')
@dory.cache(key='foo', timeout=timedelta(hours=1))
def foo(request):
    """
    Render a Foo
    """
    ...
```

### Django signals

The [Django signals](https://docs.djangoproject.com/en/stable/ref/signals/) will permit the Bloats to expire themselves when a `post_save` signal from the Bloat's Django designated model signal is sent.

```python
from dory import bloats
from .api import models

class Product(bloats.Bloat):
    """
    Product's bloat
    """
    ...

    class Meta:
        django_model = models.Product
```

```python
from dory.utils import F

@api.get('/product/<product_id>')
@bloats.Product.get(product_id=F('product_id'))
def get_product(request, product_id):
    """
    Serialize a Product
    """
    ...
```

## Roadmap

- [ ] **Bloats 🐡** (See [Bloats](#Bloats))
- [ ] **Cache utils** (See [Cache utils](#Cache-utils))
    - [ ] **Cache decorator**   
    - [ ] **Ratelimit**
- [ ] **Django signals** (See [Django signals](#Django-signals))
- [ ] **Bloats v2**
    - The v2 of the `Bloats` will implement the method `.set()`, capable not only to deprecate the current `Bloat` version, but to fill it it again. The design is still a `WIP`.
- [ ] **Support more cache engines**

## Contributing

Suggestions and contributions are extremely welcome! ❤️  
Just open an issue or a PR, and I'll respond as soon as I can.
