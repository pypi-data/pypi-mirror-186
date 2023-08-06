# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['extism']

package_data = \
{'': ['*']}

install_requires = \
['cffi>=1.10.0,<2.0.0']

setup_kwargs = {
    'name': 'extism',
    'version': '0.2.0',
    'description': 'Extism Host SDK for python',
    'long_description': '# Extism Python Host SDK\n\nSee [https://extism.org/docs/integrate-into-your-codebase/python-host-sdk/](https://extism.org/docs/integrate-into-your-codebase/python-host-sdk/).',
    'author': 'The Extism Authors',
    'author_email': 'oss@extism.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
