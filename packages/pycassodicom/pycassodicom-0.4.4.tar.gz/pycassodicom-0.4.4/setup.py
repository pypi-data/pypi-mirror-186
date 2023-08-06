# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pycassodicom']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pycassodicom',
    'version': '0.4.4',
    'description': 'De-identify dicom images by blackening pixels',
    'long_description': 'None',
    'author': 'barbara73',
    'author_email': 'barbara.jesacher@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
