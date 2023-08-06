# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lieops',
 'lieops..ipynb_checkpoints',
 'lieops.core',
 'lieops.core..ipynb_checkpoints',
 'lieops.core.combine',
 'lieops.core.combine..ipynb_checkpoints',
 'lieops.core.generators',
 'lieops.core.generators..ipynb_checkpoints',
 'lieops.linalg',
 'lieops.linalg..ipynb_checkpoints',
 'lieops.linalg.bch',
 'lieops.linalg.bch..ipynb_checkpoints',
 'lieops.linalg.congruence',
 'lieops.linalg.similarity',
 'lieops.linalg.similarity..ipynb_checkpoints',
 'lieops.solver',
 'lieops.solver..ipynb_checkpoints']

package_data = \
{'': ['*']}

install_requires = \
['mpmath>=1.2.1,<2.0.0',
 'njet>=0.3.3',
 'scipy>=1.8.0,<2.0.0',
 'sympy>=1.9,<2.0']

extras_require = \
{'docs': ['Sphinx>=4.5.0,<5.0.0',
          'sphinx-rtd-theme>=1.0.0,<2.0.0',
          'sphinxcontrib-napoleon>=0.7,<0.8']}

setup_kwargs = {
    'name': 'lieops',
    'version': '0.2.0',
    'description': 'Lie operator tools.',
    'long_description': None,
    'author': 'Malte Titze',
    'author_email': 'mtitze@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://lieops.readthedocs.io/en/latest/index.html',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
