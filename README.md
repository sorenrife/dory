<img src="https://user-images.githubusercontent.com/55748056/172958283-fa9b17c3-16a5-49e7-9a12-3d33dc5b6f6d.png" width="300">
    
Dory
====

Dory is a **Python3.8+** out-of-the box smart cache library. It simplifies multiple cache features and brings [Bloats](#Bloats) to the table, a tool designed to make smarter your application cache.

&nbsp; | Badges
--- | ---
Build | [![tests](https://github.com/sorenrife/dory/actions/workflows/test.yaml/badge.svg?branch=master&event=push)](https://github.com/sorenrife/dory/actions/workflows/test.yaml) [![build/deploy](https://github.com/sorenrife/dory/actions/workflows/deploy-prod.yaml/badge.svg)](https://github.com/sorenrife/dory/actions/workflows/deploy-prod.yaml) [![codecov](https://codecov.io/gh/sorenrife/dory/branch/master/graph/badge.svg?token=72DJGGO049)](https://codecov.io/gh/sorenrife/dory)
Docs | [![documentation](https://img.shields.io/badge/dory-docs-FF274D)](https://sorenrife.gitbook.io/dory/)
Package | [![PyPi](https://img.shields.io/pypi/v/dory-cache.svg?color=blue)](https://pypi.python.org/pypi/dory-cache/) [![PyPi versions](https://img.shields.io/pypi/pyversions/dory-cache.svg?color=blue)](https://pypi.python.org/pypi/dory-cache/) [![code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
Support | [![buy-me-a-coffee](https://img.shields.io/badge/-buy_me_a%C2%A0coffee-gray?logo=buy-me-a-coffee)](https://www.buymeacoffee.com/sorenrife)

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

More about it on the [docs](https://sorenrife.gitbook.io/dory/) 🔥

### Bloats
<p align="center">
    <img src="https://user-images.githubusercontent.com/55748056/173080628-aafb7b87-67c4-4181-9619-01ee7a4126bc.png" width="300">
</p>
<p align="center"><i>Porcupinefish have the ability to inflate their bodies by swallowing water or air, thereby becoming rounder.</i></p>
<br>

**Bloats** responds to the necessity to have a solid and clean way to define cache usage and to permit an smart cache approach to your system.
The main idea behind it is that a **Bloat** has the ability to **inflate** -as a Porcupinefish does- meaning that has the ability to cache a **key/value** given a certain configuration. Also, has the ability to **deflate** meaning exactly the contrary, that deletes the given **key/value** from the cache. Having a **Bloat** decoupled gives the application the ability to interact with the cache in a comfortable way around all the project (similar as a *Serializer* would do).


For example, let's pretend that we have a model called `Product` wich can be either renderizer or edited.  

```python
class Product(Model):
    """
    Store information about a Product
    """
    id: int = PrimaryKey()
    name: str = Text()
    description: str = Text()
```

So, to improve the `Product` performance we cache the `Product` serialization view *(GET /product)*.

```python
@api.get('/product/<id>')
@dory.cache(key=lambda request, id: "product:%s" % id, timeout=timedelta(hours=1))
def get_product(request, id) -> Response:
    """
    Serialize a Product
    """
    ...
```

Now everything works faster and as expected, but we did not contemplate that since the `Product` can be edited *(POST /product)*, we could have cached an outdated version of the `Product`, so we need a way to force the cache to refresh itself. This is where **Bloats** come in handy!  

Instead of caching the view with a custom key, decouple the cache configuration on a `Bloat`:

```python
class Product(dory.Bloat):
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
@api.get('/product/<id>')
@bloats.Product.cache(args=lambda request, id: dict(product_id=id))
def get_product(request, id) -> Response:
    """
    Serialize a Product
    """
    ...
```

And now, when a `Product` is edited, you can force the view to refresh the cache using the `Bloat` as a middle-man.

```python
@api.post('/product/<id>')
def edit_product(request, id):
    """
    Edit a Product
    """
    # edit the product
    services.product.edit(request.body)
    # clean up outdated cache
    bloats.Product(product_id=id).deflate()
```

Now your cache will always be in sync and it'll be configured in a cleaner way! 🔥

## Roadmap

- [ ] **Cache utils** (See [Cache utils](#Cache-utils))
    - [ ] **Cache decorator**   
    - [ ] **Ratelimit**
- [ ] **Bloats 🐡** (See [Bloats](#Bloats))
- [ ] **Django signals**
    ```python
    class Product(models.Model, dory.django.BloatModel):
        """
        Store information about a Product
        """
        id: int
        name: str = m.CharField(max_length=24)
        description: str = m.TextField()
    ```
    
    ```python
    @api.get('/product/<id>')
    @bloats.Product.cache(args=lambda request, id: dict(product_id=id), deflate_on=models.Product.post_save)
    def get_product(request, id):
        """
        Serialize a Product
        """
        ...
    ```
- [ ] **Bloats v2**
    - The v2 of the **Bloats** will implement the method `.reflate()`, capable not only to **deflate** the current **Bloat** but to **inflate** it again. The design is still a WIP.

## Contributing

Suggestions and contributions are extremely welcome! ❤️
Just open an issue or a PR, and I'll respond as soon as I can.
