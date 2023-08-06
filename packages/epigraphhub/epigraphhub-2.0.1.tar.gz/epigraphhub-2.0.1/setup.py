# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['epigraphhub',
 'epigraphhub.analysis',
 'epigraphhub.analysis.forecast_models',
 'epigraphhub.data',
 'epigraphhub.data.brasil',
 'epigraphhub.data.brasil.sinan',
 'epigraphhub.data.colombia',
 'epigraphhub.data.foph',
 'epigraphhub.data.owid',
 'epigraphhub.utils']

package_data = \
{'': ['*']}

install_requires = \
['GeoAlchemy2>=0.10.0,<0.11.0',
 'PyYAML>=6.0,<7.0',
 'SQLAlchemy>=1.4.29,<2.0.0',
 'arviz>=0.12.0,<0.13.0',
 'click>=8.1.0,<9.0.0',
 'geopandas>=0.10.2,<0.11.0',
 'ibis-framework>=3.2.0,<4.0.0',
 'joblib>=1.1.0,<2.0.0',
 'jupyter>=1.0.0,<2.0.0',
 'loguru>=0.6.0,<0.7.0',
 'matplotlib>=3.5.1,<4.0.0',
 'ngboost>=0.3.13,<0.4.0',
 'numpy>=1.20.3,<2.0.0',
 'pandas>=1.2,<2.0',
 'pangres>=4.1.2,<5.0.0',
 'plotly>=5,<6',
 'psycopg2-binary>=2.9.3,<3.0.0',
 'pymc>=4.2.0,<5.0.0',
 'pytrends>=4.7.3,<5.0.0',
 'requests>=2.27.1,<3.0.0',
 'rich>=12.4.4,<13',
 'rioxarray>=0.10.2,<0.11.0',
 'scikit-learn>=1.0.2,<2.0.0',
 'scipy>=1.8.0,<2.0.0',
 'sodapy>=2.2.0,<3.0.0',
 'sshtunnel>=0.4.0,<0.5.0',
 'tabulate>=0.8.9,<0.9.0',
 'tensorflow>=2.5.0,<3.0.0',
 'typer[all]>=0.4.0,<0.5.0',
 'wbgapi>=1.0.7,<2.0.0',
 'wget>=3.2,<4.0']

entry_points = \
{'console_scripts': ['epigraphhub = epigraphhub.__main__:app',
                     'epigraphhub-config = '
                     'epigraphhub.utils._config:create_file']}

setup_kwargs = {
    'name': 'epigraphhub',
    'version': '2.0.1',
    'description': 'Epigraphhub Python package',
    'long_description': '# epigraphhub_py\n\n<div align="center">\n\n[![Build status](https://github.com/thegraphnetwork/epigraphhub_py/workflows/build/badge.svg?branch=master&event=push)](https://github.com/thegraphnetwork/epigraphhub_py/actions?query=workflow%3Abuild)\n[![Python Version](https://img.shields.io/pypi/pyversions/epigraphhub.svg)](https://pypi.org/project/epigraphhub/)\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)\n[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/thegraphnetwork/epigraphhub_py/blob/master/.pre-commit-config.yaml)\n[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/thegraphnetwork/epigraphhub_py/releases)\n[![License](https://img.shields.io/github/license/thegraphnetwork/epigraphhub_py)](https://github.com/thegraphnetwork/epigraphhub_py/blob/master/LICENSE)\n![Coverage Report](assets/images/coverage.svg)\n\nEpigraphhub Python package\n\n</div>\n\nThe *EpiGraphHub library* is designed to provide external users with all of the analytical functionality used to power the [EpiGraphHub platform](https://epigraphhub.org/superset/welcome/) and its applications. In fact, all applications designed to run on the EpiGraphHub platform rely heavily on it.\n\nThis library should be used by users that want to contribute to the platform as well as by users that want to borrow some of the tools developed by our team in other opensource projects.\n\nEpiGraphHub library allows users make and apply:\n\n- Bayesian Statistics\n- Epidemiological analysis\n- Mathematical modelling\n- Cost-effectiveness analysis\n- Forecasting\n- Machine Learning\n- Text Mining\n- Geo-Spatial analysis\n\nThe EpiGraphHub library is also available for the [R](https://github.com/thegraphnetwork/r-epigraphhub/blob/main/epigraphhub.Rproj) language.\n\n## Installation\n\nThe EpigraphHub library can be installed using pip:\n\n```\n$ pip install epigraphhub\n```\n\n## Usage\nView Example EpiGraphHub Applications in Our Documentation:\n\n- [Downloading Google Trends Data (Python version)](https://epigraphhub-libraries.readthedocs.io/en/latest/data/trends.html#downloading-google-trends-data-python-version)\n- [Fetching Raster data from WorldPop](https://epigraphhub-libraries.readthedocs.io/en/latest/data/worldpop.html)\n- [Downloading data from World Bank Data](https://epigraphhub-libraries.readthedocs.io/en/latest/data/worldbank.html)\n- [Epidemiological Data Analysis](https://epigraphhub-libraries.readthedocs.io/en/latest/analysis/index.html)\n\n## Documentation\n\nThe official documentation is hosted on [ReadtheDocs](https://readthedocs.org/projects/epigraphhub-libraries/).\n\nCheck our [website](https://www.epigraphhub.org/) for most details about the EpiGraphHub project.\n\n## How to contribute\n\nIf you want to contribute to EpiGraphHub, check our [Contributing Guide](https://github.com/thegraphnetwork/epigraphhub_py/blob/main/CONTRIBUTING.md).\n\n## Code of conduct\n\nCheck our [Code of conduct](https://github.com/thegraphnetwork/epigraphhub_py/blob/main/CODE_OF_CONDUCT.md).\n\n## 📈 Releases\n\nYou can see the list of available releases on the [GitHub Releases](https://github.com/thegraphnetwork/epigraphhub_py/releases) page.\n\n## 🛡 License\n\n[![License](https://img.shields.io/github/license/thegraphnetwork/epigraphhub_py)](https://github.com/thegraphnetwork/epigraphhub_py/blob/master/LICENSE)\n\nThis project is licensed under the terms of the `GNU GPL v3.0` license. See [LICENSE](https://github.com/thegraphnetwork/epigraphhub_py/blob/master/LICENSE) for more details.\n\n## 📃 Citation\n\n```bibtex\n@misc{epigraphhub_py,\n  author = {thegraphnetwork},\n  title = {Epigraphhub Python package},\n  year = {2021},\n  publisher = {GitHub},\n  journal = {GitHub repository},\n  howpublished = {\\url{https://github.com/thegraphnetwork/epigraphhub_py}}\n}\n```\n',
    'author': 'thegraphnetwork',
    'author_email': 'fccoelho@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/thegraphnetwork/epigraphhub_py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
