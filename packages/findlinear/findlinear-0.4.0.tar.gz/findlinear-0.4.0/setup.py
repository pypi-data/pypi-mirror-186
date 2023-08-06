# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['findLinear']

package_data = \
{'': ['*']}

install_requires = \
['findpeaks>=2.4,<3.0',
 'matplotlib>=3.5.0,<4.0.0',
 'numpy>=1.20.3,<2.0.0',
 'scipy>=1.7.3,<2.0.0',
 'sympy>=1.9,<2.0']

setup_kwargs = {
    'name': 'findlinear',
    'version': '0.4.0',
    'description': 'To find the linear segment of a curve or dataset.',
    'long_description': '# `findLinear`: Determining the linear segments of data with Bayesian model comparison\n\n`findLinear` is a Python module for finding the linear segment given a curve or dataset with $x$ and $y$. \n\n## How does it work?\nIt uses the idea of Bayesian model comparison and calculate the evidence of each possible segment of curve being linear. \nAfter calculating the evidence of each segment, it detects the global maximum, or uses the `findpeaks` library to find the local maxima of evidence, from which the user can choose the relevant linear segment (e.g. that with the largest evidence, or that with the largest slope when the data consists of multiple linear segments).\n\n## Installation\nFor users, type in terminal\n```\n> pip install findLinear\n```\n\nFor developers, create a virtual environment and then type \n```\n> git clone https://git.ecdf.ed.ac.uk/s1856140/findLinear.git\n> cd findLinear \n> poetry install --with dev \n```\n\n## Quickstart\nData `x` is a list or a 1D Numpy array, sorted ascendingly; the data `y` is a list or a Numpy array, with each row being one replicate of measurement.\n```\n>>> from findLinear.findLinear import findLinear, get_example_data\n>>> x, y = get_example_data()\n>>> fl = findLinear(x, y)\n>>> fl.find_all()\n>>> fl.plot()\n>>> fl.get_argmax()\n>>> fl.get_peaks()\n```\n\n## Documentation\nDetailed documentation is available here.\n\n## Citation\n',
    'author': 'Yu Huo',
    'author_email': 'yu.huo@ed.ac.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://swainlab.bio.ed.ac.uk/software/findLinear',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
