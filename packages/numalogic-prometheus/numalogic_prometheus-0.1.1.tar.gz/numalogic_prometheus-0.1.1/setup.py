# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['numaprom', 'numaprom.udf', 'numaprom.udsink']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.25.2,<2.0.0',
 'numalogic[mlflow]>=0.3.1,<0.4.0',
 'orjson>=3.8.4,<4.0.0',
 'pynumaflow>=0.2.6,<0.3.0',
 'redis>=4.3.1,<5.0.0']

setup_kwargs = {
    'name': 'numalogic-prometheus',
    'version': '0.1.1',
    'description': 'ML inference on numaflow using numalogic on Prometheus metrics',
    'long_description': 'None',
    'author': 'Numalogic developers',
    'author_email': 'None',
    'maintainer': 'Avik Basu',
    'maintainer_email': 'avikbasu93@gmail.com',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
