# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['swimlane-stubs']

package_data = \
{'': ['*'],
 'swimlane-stubs': ['core/*',
                    'core/adapters/*',
                    'core/fields/*',
                    'core/fields/base/*',
                    'core/resources/*',
                    'utils/*']}

setup_kwargs = {
    'name': 'swimlane-stubs',
    'version': '0.3.0',
    'description': 'A small library to help with type hinting for the Swimlane Python SDK',
    'long_description': '# swimlane-stubs\n\nType stubs for [Swimlane](https://github.com/swimlane/swimlane-python).\n',
    'author': 'Alex Way',
    'author_email': 'alexwa@softcat.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
