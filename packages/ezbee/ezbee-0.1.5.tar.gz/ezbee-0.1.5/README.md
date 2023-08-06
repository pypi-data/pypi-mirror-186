# ezbee
[![pytest](https://github.com/ffreemt/ezbee/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/ezbee/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![PyPI version](https://badge.fury.io/py/ezbee.svg)](https://badge.fury.io/py/ezbee)

Align en/zh texts, fast

## Install it
**Python 3.8 only**

```shell
pip install ezbee
# or poetry add ezbee --alow-prerealeases
# pip install git+https://github.com/ffreemt/ezbee
# poetry add git+https://github.com/ffreemt/ezbee
# git clone https://github.com/ffreemt/ezbee && cd ezbee
```

## Post- or Pre-install
```
pip install fastext
pip install pyicu==2.8 pycld2
pip install https://github.com/ffreemt/ezbee/raw/main/data/artifects/polyglot-16.7.4.tar.gz
```
In linux/macos, you may need to run (if the required packages are not already present in the system) something similar to
```
apt install libicu-dev

# or for macos
brew install icu4c
brew link icu4c --force
export PKG_CONFIG_PATH="/usr/local/opt/icu4c/lib/pkgconfig"
export LDFLAGS="-L/usr/local/opt/icu4c/lib"
export CPPFLAGS="-I/usr/local/opt/icu4c/include"
```

Refer to the pre-install part in workflow file: `routine-tests.yml`

### For Windows without C++
e.g. for Python 3.8
```bash
cd data\artifects
pip install fasttext-0.9.2-cp38-cp38-win_amd64.whl pycld2-0.41-cp38-cp38-win_amd64.whl PyICU-2.8.1-cp38-cp38-win_amd64.whl
pip install https://github.com/ffreemt/ezbee/raw/main/data/artifects/polyglot-16.7.4.tar.gz
```

## Use it
```python
ezbee --help
# or python -m ezbee --help
```
