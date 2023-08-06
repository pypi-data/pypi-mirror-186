# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mathtextnlufunc']

package_data = \
{'': ['*']}

install_requires = \
['torch>=1.13.1,<2.0.0', 'transformers>=4.25.1,<5.0.0']

setup_kwargs = {
    'name': 'mathtextnlufunc',
    'version': '0.1.0',
    'description': '',
    'long_description': '### Mathtext NLU\n\nPython package to import NLU functions\n\n#### Available functions\n- sentiment\n- text2int\n',
    'author': 'Cetin CAKIR',
    'author_email': 'cetincakirtr@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
