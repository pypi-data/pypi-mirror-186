# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stabledefaults']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'stabledefaults',
    'version': '0.1.4',
    'description': 'Allows for mutable defaults comfortably and intuitively.',
    'long_description': '# Introduction\n\nstabledefaults is a small package containing a decorator to allow for the expected behavior of lists, dicts and other mutable arguments in default arguments.\n\n## Explanation\n\nIn Python, functions (as anything else) are objects, and the default arguments are stored as attributes that are initialized in definition.\n\nOnce this is known and the person understands that variables are references in Python, then it is relatively straightforward to understand the following behavior:\n\n```python\ndef f(x=[]):\n    x.append(2)\n    return x\n```\n\n```python\n>>> a = f()\n>>> a\n[2]\n>>> f()\n>>> a\n[2, 2]\n```\n\nNevertheless, this is unintuitive. Not only that, but dealing with this requires things such as\n```python\ndef f(x = None):\n    if x is None:\n        x = []\n\n    x.append(2)\n    return x\n```\nwhich forces types such as ```list | None``` where just ```list``` should suffice, and also forces code inside the function itself.\n\nThis package solves this issue with a decorator. For instance, the example above would become\n```python\n@stabledefaults()\ndef f(x=[]):\n    x.append(2)\n    return x\n```\n```python\n>>> a = f()\n>>> a\n[2]\n>>> f()\n>>> a\n[2]\n```',
    'author': 'AloizioMacedo',
    'author_email': 'atsam2@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/AloizioMacedo/stabledefaults',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
