# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gen_trace']

package_data = \
{'': ['*']}

install_requires = \
['icecream>=2.1.1,<3.0.0',
 'install>=1.3.5,<2.0.0',
 'logzero>=1.7.0,<2.0.0',
 'matplotlib>=3.6.2,<4.0.0',
 'nptyping>=2.4.1,<3.0.0',
 'numpy>=1.24.1,<2.0.0',
 'scikit-learn>=1.2.0,<2.0.0',
 'set-loglevel>=0.1.2,<0.2.0',
 'typer>=0.4.1,<0.5.0']

entry_points = \
{'console_scripts': ['gen-trace = gen_trace.__main__:app']}

setup_kwargs = {
    'name': 'gen-trace',
    'version': '0.1.0',
    'description': 'Generate interpolate1d (trace) for a cmat',
    'long_description': '# gen-trace\n[![pytest](https://github.com/ffreemt/gen-trace/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/gen-trace/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/gen-trace.svg)](https://badge.fury.io/py/gen-trace)\n\nGenerate interpolate1d (trace) for a cmat\n\n**For python 3.8 only** (contact the dev concerning other python versions)\n\n## Install it\n\n```shell\npip install gen-trace\n# pip install git+https://github.com/ffreemt/gen-trace\n# poetry add git+https://github.com/ffreemt/gen-trace\n# git clone https://github.com/ffreemt/gen-trace && cd gen-trace\n```\n\n## Use it\n```python\nfrom gen_trace.cmat2aset import cmat2aset\n\n```\n',
    'author': 'ffreemt',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ffreemt/gen-trace',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.3,<4.0.0',
}


setup(**setup_kwargs)
