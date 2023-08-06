# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ezbee']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.1,<4.0.0',
 'Morfessor>=2.0.6,<3.0.0',
 'XlsxWriter>=3.0.3,<4.0.0',
 'cchardet>=2.1.7,<3.0.0',
 'environs>=9.5.0,<10.0.0',
 'fast-scores>=0.1.3,<0.2.0',
 'gen-trace>=0.1.0a2,<0.1.0',
 'icecream>=2.1.1,<3.0.0',
 'install>=1.3.5,<2.0.0',
 'logzero>=1.7.0,<2.0.0',
 'typer>=0.4.0,<0.5.0']

extras_require = \
{'plot': ['holoviews>=1.14.8,<2.0.0',
          'plotly>=5.6.0,<6.0.0',
          'seaborn>=0.11.2,<0.12.0']}

entry_points = \
{'console_scripts': ['ezbee = ezbee.__main__:app']}

setup_kwargs = {
    'name': 'ezbee',
    'version': '0.1.4',
    'description': 'english-chinese dualtext aligner',
    'long_description': '# ezbee\n[![pytest](https://github.com/ffreemt/ezbee/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/ezbee/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![PyPI version](https://badge.fury.io/py/ezbee.svg)](https://badge.fury.io/py/ezbee)\n\nAlign en/zh texts, fast\n\n## Install it\n**Python 3.8 only**\n\n```shell\npip install ezbee\n# or poetry add ezbee --alow-prerealeases\n# pip install git+https://github.com/ffreemt/ezbee\n# poetry add git+https://github.com/ffreemt/ezbee\n# git clone https://github.com/ffreemt/ezbee && cd ezbee\n```\n\n## Post- or Pre-install\n```\npip install fastext\npip install pyicu==2.8 pycld2\npip install https://github.com/ffreemt/ezbee/raw/main/data/artifects/polyglot-16.7.4.tar.gz\n```\nIn linux/macos, you may need to run (if the required packages are not already present in the system) something similar to\n```\napt install libicu-dev\n\n# or for macos\nbrew install icu4c\nbrew link icu4c --force\nexport PKG_CONFIG_PATH="/usr/local/opt/icu4c/lib/pkgconfig"\nexport LDFLAGS="-L/usr/local/opt/icu4c/lib"\nexport CPPFLAGS="-I/usr/local/opt/icu4c/include"\n```\n\nRefer to the pre-install part in workflow file: `routine-tests.yml`\n\n### For Windows without C++\ne.g. for Python 3.8\n```bash\ncd data\\artifects\npip install fasttext-0.9.2-cp38-cp38-win_amd64.whl pycld2-0.41-cp38-cp38-win_amd64.whl PyICU-2.8.1-cp38-cp38-win_amd64.whl\npip install https://github.com/ffreemt/ezbee/raw/main/data/artifects/polyglot-16.7.4.tar.gz\n```\n\n## Use it\n```python\nezbee --help\n# or python -m ezbee --help\n```\n',
    'author': 'ffreemt',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ffreemt/ezbee',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8.3,<4.0.0',
}


setup(**setup_kwargs)
