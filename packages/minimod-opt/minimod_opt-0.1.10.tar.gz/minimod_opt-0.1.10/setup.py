# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['minimod_opt',
 'minimod_opt.base',
 'minimod_opt.continuous',
 'minimod_opt.monte_carlo',
 'minimod_opt.solvers',
 'minimod_opt.tests',
 'minimod_opt.utils']

package_data = \
{'': ['*'], 'minimod_opt.continuous': ['example/*']}

install_requires = \
['adjustText>=0.7.3,<0.8.0',
 'matplotlib>=3.6.1,<4.0.0',
 'mip==1.9.3',
 'numpy>=1.23.4,<2.0.0',
 'pandas>=1.5.0,<2.0.0',
 'pqdm>=0.2.0,<0.3.0',
 'progressbar33>=2.4,<3.0',
 'python-docx>=0.8.11,<0.9.0',
 'tabulate>=0.9.0,<0.10.0',
 'xlrd>=2.0.1,<3.0.0']

setup_kwargs = {
    'name': 'minimod-opt',
    'version': '0.1.10',
    'description': 'A mixed-integer program optimization solver for finding optimal nutritional interventions across space and time.',
    'long_description': '# minimod-opt\nA mixed-integer solver that solves optimal intervention allocation across time and space (Port from GAMS)\n\nThis python module is designed as a port from GAMS and uses `mip` to do mixed-integer optimization.\n\nVisit [the website](https://minimod-nutrition.github.io/minimod) for more information!\n',
    'author': 'Aleksandr Michuda',
    'author_email': 'am2497@cornell.edu',
    'maintainer': 'Aleksandr Michuda',
    'maintainer_email': 'am2497@cornell.edu',
    'url': 'https://minimod-nutrition.github.io/minimod-opt/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
