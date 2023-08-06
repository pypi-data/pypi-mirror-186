# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cucumber_expressions']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cucumber-expressions',
    'version': '16.1.2',
    'description': 'Cucumber Expressions - a simpler alternative to Regular Expressions',
    'long_description': "# Cucumber Expressions for Python\n\n[The main docs are here](https://github.com/cucumber/cucumber-expressions#readme).\n\n## Build system\n\nThis project uses [Poetry](https://python-poetry.org/) as its build system.\nIn order to develop on this project, please install Poetry as per your system's instructions on the link above.\n\n## Tests\n\nThe test suite uses `pytest` as its testing Framework.\n\n\n### Preparing to run the tests\n\nIn order to set up your dev environment, run the following command from this project's directory:\n\n``` python\npoetry install\n```\nIt will install all package and development requirements, and once that is done it will do a dev-install of the source code.\n\nYou only need to run it once, code changes will propagate directly and do not require running the install again.\n\n\n### Running the tests\n\n`pytest` automatically picks up files in the current directory or any subdirectories that have the prefix or suffix of `test_*.py`.\nTest function names must start with `test*`.\nTest class names must start with `Test*`.\n\nTo run all tests:\n\n``` python\npoetry run pytest\n```\n\n",
    'author': 'Jason Allen',
    'author_email': 'jsa34@noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cucumber/cucumber-expressions',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
