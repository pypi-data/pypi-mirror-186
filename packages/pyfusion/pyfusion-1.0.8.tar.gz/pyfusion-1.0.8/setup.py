# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fusion', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.1',
 'fsspec>=2021.6.1',
 'joblib>=1.1.0',
 'pandas>1.1.1',
 'pyarrow>=4.0',
 'requests>2.27.0',
 'tabulate>=0.8.10',
 'tqdm>=4.64.0',
 'types-requests>2.27.0',
 'types-tabulate>=0.8.8']

extras_require = \
{'dev': ['pytest>=6.2.4,<7.0.0',
         'pytest-cov>=2.12.0,<3.0.0',
         'tox>=3.20.1,<4.0.0',
         'tox-conda>=0.8.2,<0.9.0',
         'virtualenv>=20.2.2,<21.0.0',
         'pip>=20.3.1,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'pre-commit>=2.12.0,<3.0.0',
         'toml>=0.10.2,<0.11.0',
         'bump2version>=1.0.1,<2.0.0'],
 'doc': ['mkdocs>=1.2.3,<2.0.0',
         'mkdocs-material>=8.1.0,<9.0.0',
         'mkdocstrings>=0.16.0,<0.17.0',
         'mkdocs-autorefs>=0.2.1,<0.3.0',
         'mkdocs-include-markdown-plugin>=2.8.0,<3.0.0',
         'mkdocs-git-revision-date-plugin>=0.3.1,<0.4.0',
         'mkdocs-jupyter>=0.22.0,<0.23.0',
         'jupyter_contrib_nbextensions>=0.7.0,<0.8.0',
         'mike>=1.1.2,<2.0.0'],
 'test': ['black>=22.3.0,<23.0.0',
          'isort>=5.8.0,<6.0.0',
          'flake8>=3.9.2,<4.0.0',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'mypy>=0.900,<0.901',
          'pytest>=6.2.4,<7.0.0',
          'pytest-cov>=2.12.0,<3.0.0']}

setup_kwargs = {
    'name': 'pyfusion',
    'version': '1.0.8',
    'description': 'JPMC Fusion Developer Tools',
    'long_description': "# PyFusion #\n\nPyFusion is the Python SDK for the Fusion platform API. \n\n## Installation\n\n```bash\npip install pyfusion\n```\n\nFusion by J.P. Morgan is a cloud-native data platform for institutional investors, providing end-to-end data management, analytics, and reporting solutions across the investment lifecycle. The platform allows clients to seamlessly integrate and combine data from multiple sources into a single data model that delivers the benefits and scale and reduces costs, along with the ability to more easily unlock timely analysis and insights. Fusion's open data architecture supports flexible distribution, including partnerships with cloud and data providers, all managed by J.P. Morgan data experts. \n\nFor more information, please visit [fusion.jpmorgan.com](https://fusion.jpmorgan.com)\n\nFor the SDK documentation, please visit [page](https://jpmorganchase.github.io/fusion)\n\n\n\n",
    'author': 'FusionDevs',
    'author_email': 'fusion_developers@jpmorgan.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jpmorganchase/fusion',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<4.0',
}


setup(**setup_kwargs)
