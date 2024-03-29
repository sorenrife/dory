<p align="center">
    <img src="https://user-images.githubusercontent.com/55748056/172958283-fa9b17c3-16a5-49e7-9a12-3d33dc5b6f6d.png" width="300">
</p>

<p align="center">
  <a href="https://github.com/sorenrife/dory/actions/workflows/deploy.yaml">
    <img src="https://github.com/sorenrife/dory/actions/workflows/deploy.yaml/badge.svg">
  </a>
  <a href="https://codecov.io/gh/sorenrife/dory">
    <img src="https://codecov.io/gh/sorenrife/dory/branch/master/graph/badge.svg?token=72DJGGO049"/>
  </a>
  <a href="https://pypi.python.org/pypi/dory-cache/">
    <img src="https://img.shields.io/pypi/v/dory-cache.svg?color=blue">
  </a>
  <a>
      <img src="https://img.shields.io/pypi/pyversions/dory-cache.svg?color=blue">
  </a>
  <br/>
  <a href="https://github.com/sorenrife/dory/blob/main/LICENSE.md">
    <img src="https://img.shields.io/badge/License-MIT-lightgrey.svg"
         alt="License: MIT">
  </a>
  <a href="https://github.com/sponsors/sorenrife">
    <img src="https://img.shields.io/badge/GitHub-Become a sponsor-orange.svg"
         alt="GitHub: Become a sponsor">
  </a>
  <a href="https://www.buymeacoffee.com/sorenrife">
    <img src="https://img.shields.io/badge/-buy_me_a%C2%A0coffee-gray?logo=buy-me-a-coffee"
         alt="Buy me a coffeee">
  </a>
</p>

<p align="center">
  <a href="#installation">Installation</a>
  • <a href="#features">Features</a>
  • <a href="README.md#usage">Usage</a>
  • <a href="#roadmap">Roadmap</a>
  • <a href="#contributing">Contributing</a>
</p>

-----------------------

<p align="center">
The modern <b>Python3.8+</b> out-of-the-box reactive cache solution
</p>

-----------------------

## Installation

Installation is as simple as:

```bash
pip install dory-cache
```

View the current documentation [here](https://sorenrife.gitbook.io/dory/)

## Usage

Dory's configuration is quite simple. On your project initialization just
call the setup function as follows

```python
from dory.setup import setup

setup(
    host=REDIS_HOST,
    port=REDIS_PORT,
    user=REDIS_USER,
    password=REDIS_PASSWORD
)
```


## Features

### Bloats

`Bloats` responds to the need of having a simpler approach on designing reactive cache on your system.
**They make cache configuration and management easy.**

For example, let's pretend that we have a model called `Product` which can be either serialized or edited. So, to improve the `Product` serialization performance we cache the `Product` serialization view **(GET /product/<id>)**.

```python
from dory.cache import cache
from dory.utils import F

@api.get('/product/<product_id>')
@cache(key=F('product_id'), timeout=timedelta(hours=1))
def get_product(request, product_id):
    """
    Serialize a Product
    """
    ...
```

Now everything works faster and as expected, but we did not contemplate that since the `Product` can be edited **(PUT /product/<id>)**, we could have cached an outdated version of the `Product`, so we need a way to force the cache to refresh itself. This is where **Bloats** come in handy!

Instead of caching the view with a generic cache decorator, decouple the cache configuration on a `Bloat`

```python
from dory.bloats import Bloat, Field

class Product(Bloat):
    """
    Product's bloat
    """
    product_id: int = Field(...)
    
    class Options:
        timeout: timedelta = timedelta(hours=1)
        enabled: bool = True
```

```python
from dory.bloats.utils import F, cache

@api.get('/product/<product_id>')
@cache(Product(product_id=F('product_id')))
def get_product(request, product_id):
    """
    Serialize a Product
    """
    ...
```

And now, when a `Product` is edited, you can force the view to refresh the cache using the `Bloat` as a middle-man.

```python
from dory.bloats.utils import F, destroy

@api.put('/product/<product_id>')
@destroy(Product(product_id=F('product_id')))
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
from dory.cache import cache
from dory.utils import F

@api.get('/foo')
@cache(key=F('foo_id'), timeout=timedelta(hours=1))
def foo(request, foo_id):
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
@cache(Product(product_id=F('product_id')))
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
