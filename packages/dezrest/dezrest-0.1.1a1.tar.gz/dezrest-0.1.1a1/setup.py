# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dezrest']

package_data = \
{'': ['*']}

install_requires = \
['ezbee>=0.1.5,<0.2.0',
 'fastapi>=0.88.0,<0.89.0',
 'logzero>=1.7.0,<2.0.0',
 'pybind11>=2.10.1,<3.0.0',
 'seg-text>=0.1.2,<0.2.0',
 'set-loglevel>=0.1.2,<0.2.0',
 'uvicorn[standard]>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['dezrest = dezrest.__main__:app_typer']}

setup_kwargs = {
    'name': 'dezrest',
    'version': '0.1.1a1',
    'description': 'serve ez/dz/de bee via FastAPI rest',
    'long_description': '# dezbee-rest\n[![pytest](https://github.com/ffreemt/dezbee-rest/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/dezbee-rest/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/dezrest.svg)](https://badge.fury.io/py/dezrest)\n\nServe ezbee via FastAPI port 5555 ([de|dz]bee may be supported later)\n\n## Install it (Python 3.8 only)\n\n```shell\npip install dezrest\n\n# pip install git+https://github.com/ffreemt/dezbee-rest\n# poetry add git+https://github.com/ffreemt/dezbee-rest\n# git clone https://github.com/ffreemt/dezbee-rest && cd dezbee-rest\n```\n\n### Python virutal environment (Optional)\nYou may wish to create a python virutal environment first, e.g.,\n```\nmkdir temp-dir && cd temp-dir\npy -3.8 -m venv .venv\ncall .venv\\Scripts\\activate\npip install dezrest\n```\n\n## Post- or Pre-install (same as for ezbee)\n```\npip install fastext\npip install pyicu==2.8 pycld2\npip install https://github.com/ffreemt/ezbee/raw/main/data/artifects/polyglot-16.7.4.tar.gz\n```\nIn linux/macos, you may need to run (if the required packages are not already present in the system) something similar to\n```\napt install libicu-dev\n\n# or for macos\nbrew install icu4c\nbrew link icu4c --force\nexport PKG_CONFIG_PATH="/usr/local/opt/icu4c/lib/pkgconfig"\nexport LDFLAGS="-L/usr/local/opt/icu4c/lib"\nexport CPPFLAGS="-I/usr/local/opt/icu4c/include"\n```\n\nRefer to the `pre-install` part in workflow file [`routine-tests.yml`](https://github.com/ffreemt/dezbee-rest/blob/main/.github/workflows/routine-tests.yml)\n\n\n## Use it\n\n```bash\n# sart the server at port 5555 via `uvicorn` with 2 workers\npython -m dezrest\n\n# or\ndezrest\n\n# or run at external IP\npython -m dezrest --host 0.0.0.0\n\n# or dezrest --host 0.0.0.0\n\n# cli help\npython -m dezrest --help\n\n# or\ndezrest --help\n\n# REST docs (Swagger UI)\nhttp://127.0.0.1:5555/docs\n\n```\n\n### Sample run:\n```\n$ dezrest\n[D 221220 10:48:21 fastlid:34] fetching lid.176.ftz (once only)\n[I 221220 10:48:22 fastlid:44] Downloading https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz (need to do this just once)\n[I 221220 10:48:27 __main__:204]  pid: C:\\mat-dir\\playground\\venv-python\nINFO:     Uvicorn running on http://127.0.0.1:5555 (Press CTRL+C to quit)\nINFO:     Started parent process [486952]\nINFO:     Started server process [548488]\nINFOINFO:     Started server process [:     Waiting for application startup.\n547296]\nINFOINFO:     Application startup complete.\n:     Waiting for application startup.\nINFO:     Application startup complete.\nINFO:     127.0.0.1:7114 - "POST /post/ HTTP/1.1" 200 OK\nINFO:     Shutting down\nINFO:     Waiting for application shutdown.\nINFO:     Application shutdown complete.\nINFO:     Finished server process [547296]\n```\n\nTo kill the server in Windows, kill the parent process (CTRL+C does not quite work in Windows at least), e.g.\n```\ntaskkill /f /pid 486952\n```\n\n### Test the REST API:\n```python\nimport httpx\nres = httpx.post("http://127.0.0.1:5555/post/", json=["test\\nlove", "没有\\n测试\\n其他\\n爱"]).json()\nprint(res)\n# [[\'\', \'没有\', \'\'], [\'test\', \'测试\', \'0.75\'], [\'\', \'其他\', \'\'], [\'love\', \'爱\', \'0.87\']]\n\n```',
    'author': 'ffreemt',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ffreemt/dezbee-rest',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.3,<4.0.0',
}


setup(**setup_kwargs)
