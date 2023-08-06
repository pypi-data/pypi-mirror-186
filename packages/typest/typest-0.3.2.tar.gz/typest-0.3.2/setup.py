# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['typest', 'typest.outcomes', 'typest.typecheckers', 'typest.utils']

package_data = \
{'': ['*']}

install_requires = \
['comment-parser>=1.2.4,<2.0.0', 'mypy>=0.991,<0.992', 'pyright>=1.1,<2.0']

setup_kwargs = {
    'name': 'typest',
    'version': '0.3.2',
    'description': 'A framework for testing type expectations',
    'long_description': '# typest\n\n[![pypi](https://img.shields.io/pypi/v/typest.svg)](https://pypi.python.org/pypi/typest)\n[![versions](https://img.shields.io/pypi/pyversions/typest.svg)](https://github.com/jonathan-scholbach/typest)\n\nAn experimental framework to test your library against type checkers, allowing\nto formulate type expectations and expected typechecker errors. Its purpose is\nthe same as the one of\n[pytest-mypy-plugins](https://pypi.org/project/pytest-mypy-plugins/). While\n`pytest-mypy-plugins` requires `.yaml` files for specifying the tests, `typest`\ntest cases are python files, expectations are formulated in comments:\n\n\n```Python\nfrom mylibrary import some_function\n\nresult = some_function()\n\nreveal_type(result)  # expect-type: int\n```\n\n\nBesides expressing type expectations, you can also specify to expect an error\nfrom the typechecker:\n\n```Python\nstring: str = "not a number"\nnumber: int = string  # expect-error\n```\n\n\nYou can also specify to expect a mismatch error, i.e. an error where an assigned\ntype is mismatching the actual type:\n\n```Python\nstring: str = "not a number"\nnumber: int = string  # expect-mismatch: int <> str\n```\n\n## Suppported Typecheckers\n\n+ `mypy`\n+ `pyright`\n\n\n## Installation\n\n`typest` is available at pypi. You can install it through pip:\n\n    pip install typest\n\n\n## Use\n\n    python -m typest [PATH] [TYPECHECKERS]\n\nIf PATH is a directory, all python files under that directory (including\nsubdirectories) are going to be checked. If PATH points to a file, it has to be\na python file.\n\n\nTYPECHECKERS is an optional argument, a comma separated list of names of\ntypecheckers you want to run your tests against. Currently, `mypy` and `pyright`\nare suppported.\n\n\n## Development\n\nYou can add more typecheckers by subclassing\n`typest.typecheckers.base.TypeChecker` and importing your new class in\n`typest/typecheckers/__init__.py`.\n',
    'author': 'Jonathan Scholbach',
    'author_email': 'j.scholbach@posteo.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jonathan-scholbach/typest',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
