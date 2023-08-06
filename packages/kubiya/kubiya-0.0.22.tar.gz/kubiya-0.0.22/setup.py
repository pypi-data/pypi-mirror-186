# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kubiya']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.79.0,<0.80.0',
 'jsonschema==4.17.3',
 'pydantic==1.10.2',
 'uvicorn>=0.18.2,<0.19.0']

setup_kwargs = {
    'name': 'kubiya',
    'version': '0.0.22',
    'description': 'Kubiya is a DevOps virtual assistant that captures and converts organizational knowledge into self-service workflows for a delightful business, IT and Cloud operations experience.',
    'long_description': 'None',
    'author': 'Kubiya',
    'author_email': 'info@kubiya.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>3.7.2,<3.12',
}


setup(**setup_kwargs)
