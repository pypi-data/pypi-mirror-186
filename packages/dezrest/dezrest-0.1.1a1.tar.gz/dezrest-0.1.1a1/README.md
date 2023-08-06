# dezbee-rest
[![pytest](https://github.com/ffreemt/dezbee-rest/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/dezbee-rest/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/dezrest.svg)](https://badge.fury.io/py/dezrest)

Serve ezbee via FastAPI port 5555 ([de|dz]bee may be supported later)

## Install it (Python 3.8 only)

```shell
pip install dezrest

# pip install git+https://github.com/ffreemt/dezbee-rest
# poetry add git+https://github.com/ffreemt/dezbee-rest
# git clone https://github.com/ffreemt/dezbee-rest && cd dezbee-rest
```

### Python virutal environment (Optional)
You may wish to create a python virutal environment first, e.g.,
```
mkdir temp-dir && cd temp-dir
py -3.8 -m venv .venv
call .venv\Scripts\activate
pip install dezrest
```

## Post- or Pre-install (same as for ezbee)
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

Refer to the `pre-install` part in workflow file [`routine-tests.yml`](https://github.com/ffreemt/dezbee-rest/blob/main/.github/workflows/routine-tests.yml)


## Use it

```bash
# sart the server at port 5555 via `uvicorn` with 2 workers
python -m dezrest

# or
dezrest

# or run at external IP
python -m dezrest --host 0.0.0.0

# or dezrest --host 0.0.0.0

# cli help
python -m dezrest --help

# or
dezrest --help

# REST docs (Swagger UI)
http://127.0.0.1:5555/docs

```

### Sample run:
```
$ dezrest
[D 221220 10:48:21 fastlid:34] fetching lid.176.ftz (once only)
[I 221220 10:48:22 fastlid:44] Downloading https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz (need to do this just once)
[I 221220 10:48:27 __main__:204]  pid: C:\mat-dir\playground\venv-python
INFO:     Uvicorn running on http://127.0.0.1:5555 (Press CTRL+C to quit)
INFO:     Started parent process [486952]
INFO:     Started server process [548488]
INFOINFO:     Started server process [:     Waiting for application startup.
547296]
INFOINFO:     Application startup complete.
:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:7114 - "POST /post/ HTTP/1.1" 200 OK
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [547296]
```

To kill the server in Windows, kill the parent process (CTRL+C does not quite work in Windows at least), e.g.
```
taskkill /f /pid 486952
```

### Test the REST API:
```python
import httpx
res = httpx.post("http://127.0.0.1:5555/post/", json=["test\nlove", "没有\n测试\n其他\n爱"]).json()
print(res)
# [['', '没有', ''], ['test', '测试', '0.75'], ['', '其他', ''], ['love', '爱', '0.87']]

```