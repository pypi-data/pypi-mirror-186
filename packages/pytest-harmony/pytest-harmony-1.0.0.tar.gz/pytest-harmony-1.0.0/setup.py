# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_harmony']

package_data = \
{'': ['*']}

install_requires = \
['Sphinx>=4.4.0,<5.0.0',
 'black>=22.6.0,<23.0.0',
 'furo>=2022.1.2,<2023.0.0',
 'isort>=5.10.1,<6.0.0',
 'pytest-asyncio>=0.20.3,<0.21.0',
 'pytest>=7.2.1,<8.0.0',
 'sphinx-copybutton>=0.4.0,<0.5.0',
 'taskipy>=1.9.0,<2.0.0',
 'typing-extensions>=4.4.0,<5.0.0']

setup_kwargs = {
    'name': 'pytest-harmony',
    'version': '1.0.0',
    'description': 'Chain tests and data with pytest',
    'long_description': '# Pytest harmony\nA library to make test trees.  \n\n## What is test chains?\n- Test 1 starts  \n- Test 1 finishes, output goes to all depending tests  \n  - Test 2 starts with output from test 1  \n  - Test 2 finishes, output goes to all depending tests  \n    - Test 3 starts  \n    - Test 3 fails, depending tests gets skipped  \n    - Test 3 cleanup gets called  \n  - Test 2 cleanup gets called  \n- Test 1 cleanup gets called  \n',
    'author': 'TAG-Epic',
    'author_email': 'tagepicuwu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
