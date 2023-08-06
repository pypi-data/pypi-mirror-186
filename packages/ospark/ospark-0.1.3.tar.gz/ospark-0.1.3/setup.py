# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ospark',
 'ospark.backbone',
 'ospark.data',
 'ospark.data.generator',
 'ospark.models',
 'ospark.nn',
 'ospark.nn.block',
 'ospark.nn.cell',
 'ospark.nn.component',
 'ospark.nn.layers',
 'ospark.nn.loss_function',
 'ospark.nn.metrics',
 'ospark.nn.optimizer',
 'ospark.ocr',
 'ospark.predictor',
 'ospark.samples',
 'ospark.trainer',
 'ospark.utility',
 'ospark.validator']

package_data = \
{'': ['*']}

install_requires = \
['tensorflow>=2.7.0,<3.0.0']

setup_kwargs = {
    'name': 'ospark',
    'version': '0.1.3',
    'description': 'Ospark is an opensource for quickly builder of former model series.',
    'long_description': None,
    'author': 'ospark-org',
    'author_email': 'donggicai1991@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
