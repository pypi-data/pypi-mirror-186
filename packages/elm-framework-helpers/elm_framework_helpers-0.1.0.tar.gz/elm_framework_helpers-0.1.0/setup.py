# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['elm_framework_helpers', 'elm_framework_helpers.output']

package_data = \
{'': ['*']}

install_requires = \
['reactivex>=4.0.4,<5.0.0']

setup_kwargs = {
    'name': 'elm-framework-helpers',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Mat',
    'author_email': 'mathieu@redapesolutions.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/TechSpaceAsia/elm-framework-helpers',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
