# Rest tool
> > A curated list of awesome things related to microservices and computer vision.

This module contains interesting features for endpoint creation. It also includes some decorators.

## Details

- Decorest [Decorator that allows implementing a general try_log function in the entire function, but it is necessary to use the ResData data model.]

## Installation

Use the package manager pip to install restutil.

```bash
pip install restutil
```

## Usage

```python
from restutil.decorators import Decorest

# create deco object
deco = Decorest()

# wrap foo function
@deco.try_log
def foo():
    return None
```

## Author

- Adonis Gonzalez Godoy - [LinkedIn](https://www.linkedin.com/in/adonis-gonzalez) -  [E-mail](adions025@gmail.com)