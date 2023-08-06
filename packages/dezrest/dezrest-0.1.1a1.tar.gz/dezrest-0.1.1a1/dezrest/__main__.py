r"""Serve ezbee via post port default 5555.

```bash
In: [str, str]
Out: List[Tuple[str, str, str]]

Tests:
curl -X 'POST' \
  'http://127.0.0.1:5555/post/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text1": "string",
  "text2": "string"
}'

res = httpx.post("http://127.0.0.1:5555/post/", json={'text1': 'a', 'text2': 'b'})
# res.json() = {'res': [['a', 'b', ''], ['c', 'c', '0.5']]}

x httpx.post("http://127.0.0.1:5555/post/", json=['a', 'b']).json()
httpx.post("http://127.0.0.1:5555/post/", json={'texts': ['a', 'b']}).json()

var r = await axios.post(`http://127.0.0.1:5555/post/`, { text1: 'a', text2: 'b' })
var r = await axios.post(`http://127.0.0.1:5555/post/`, { texts: ['a', 'b'] })
r.data
// { res: [ [ 'a', 'b', '' ], [ 'c', 'c', '0.5' ] ] }

Modified accordingly (remove text1, text2 and used list directly):
httpx.post("http://127.0.0.1:5555/post/", json=['a', 'b']).json()
# Out: [['a', 'b', '0.0']]

httpx.post("http://127.0.0.1:5555/post/", json=['test\nlove', '没有\n测试\n爱']).json()
# Out: [['', '没有', ''], ['test', '测试', '0.74'], ['love', '爱', '0.86']]

httpx.post("http://127.0.0.1:5555/post/", json=['test\nlove', '没有\n测试\n其他\n爱']).json()
# Out: [['', '没有', ''], ['test', '测试', '0.75'], ['', '其他', ''], ['love', '爱', '0.87']]
```
Modify API to take `split2sents` parameter
```
httpx.post("http://127.0.0.1:5555/post/", json={"texts": ['test\nlove', '没有\n测试\n其他\n爱',]}).json()
httpx.post("http://127.0.0.1:5555/post/",
    json={"texts": ['test\nlove', '没有\n测试\n其他\n爱',], "split2sents": True}).json()
# Out: [['', '没有', ''], ['test', '测试', '0.75'], ['', '其他', ''], ['love', '爱', '0.87']]
```
"""
# pylint: disable=invalid-name, too-few-public-methods
# sanic sanic-app:app or sanic sanic-app.app
# http://127.0.0.1:8000
# from icecream import ic
# pylint: disable=invalid-name, no-name-in-module, unused-import
# import json
import os

# import signal
# from signal import SIG_DFL, SIGINT, signal
from typing import List, Optional, Tuple, Union

import logzero
import typer
import uvicorn

# from time import sleep
from ezbee import ezbee
from ezbee.gen_pairs import gen_pairs
from ezbee.save_xlsx_tsv_csv import save_xlsx_tsv_csv
from fastapi import FastAPI
from logzero import logger
from pydantic import BaseModel
from seg_text import seg_text
from set_loglevel import set_loglevel

from dezrest import __version__

# import sys
# from argparse import Namespace  # from types import SimpleNamespace
# from pathlib import Path

# from sanic.log import logger

# from sanic import Sanic, response
# from sanic.response import text
# from sanic.exceptions import ServerError, NotFound


logzero.loglevel(set_loglevel())

# app = Sanic("MyHelloWorldApp")
# debug = True
# port = 5555

app = FastAPI(
    title="dezbee-rest",
    version=__version__,
    description=f"{__doc__}",
)

app_typer = typer.Typer(
    name="dezrest",
    add_completion=False,
    help="serve ez/de/dzbee via rest default port 5555",
)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{app.title} v.{__version__} -- ...")
        raise typer.Exit()


@app.get("/")
async def hello_world():
    """Trivial template."""
    # ic(request)
    # ic(request.args)
    # return text("Hello, world.")
    return {"greetings": "Hello from dezbee-rest"}


class ThreeCols(BaseModel):
    """Define response_model (not used)."""

    __root__: List[Tuple[str, str, Union[str, float]]]


# @app.post("/post/", response_model=ThreeCols)
# def on_post(texts: Texts):


class Inputs(BaseModel):
    """Define request body (not used)."""

    texts: Tuple[str, str]
    split2sents: Union[bool, None] = None


@app.post("/post/", response_model=List[Tuple[str, str, str]])
# def on_post(inputs: Tuple[str, str, bool]):  # text1, text2, splitToSents
def on_post(inputs: Inputs):  # text1, text2, splitToSents
    """Deliver aligned pairs.

    ```
    Request body: [str, str, bool]

    Response model: List[Tuple[str, str, str]]
    """
    # logger.debug(" d texts: %s", texts)

    # text1, text2, split2sents = inputs
    text1, text2 = inputs.texts
    list1, list2 = text1.splitlines(), text2.splitlines()

    # list1, list2 = text1.splitlines(), text2.splitlines()
    # logger.debug("type(list1): %s, list1[:5]: %s", type(list1), list1[:5])
    # logger.debug("type(list2): %s, list2[:5]: %s", type(list2), list2[:5])

    # aset = ezbee(lines1, lines2)
    # aset = ezbee(list1, list2)

    if inputs.split2sents:
        list1 = seg_text(list1)
        list2 = seg_text(list2)

    aset = ezbee(list1, list2)

    logzero.loglevel(set_loglevel())
    if aset:
        logger.debug("aset: %s...%s", aset[:4], aset[-4:])
        # logger.debug("aset: %s", aset)

    # aligned_pairs = gen_pairs(list1, list2, aset)
    aligned_pairs = gen_pairs(list1, list2, aset)

    logger.debug("aligned_pairs[:5]: %s", aligned_pairs[:5])

    _ = """
    return [
        ['a', 'b', ''],
        ['c', 'd', .5],
    ]
    # """

    return aligned_pairs


@app_typer.command()
def main(
    host: str = typer.Option(  # pylint: disable=(unused-argument
        "127.0.0.1",
        "--host",
        "-h",
        help="Set host, e.g., 0.0.0.0, or an external IP.",
    ),
    port: int = typer.Option(
        5555,
        "--port",
        "-p",
        help="Set port that is not currently in use.",
    ),
    version: Optional[bool] = typer.Option(  # pylint: disable=(unused-argument
        None,
        "--version",
        "-v",
        "-V",
        help="Show version info and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
):
    """Run the whole thing."""
    if set_loglevel() <= 10:
        reload = True
        workers = 1
    else:
        reload = False
        workers = 2

    logger.info(" pid: %s ", os.getcwd())

    uvicorn.run(
        # app,
        "dezrest.__main__:app",
        # host='0.0.0.0',
        # host='127.0.0.1',
        host=host,
        port=port,
        reload=reload,
        workers=workers,
        # debug=True,
        timeout_keep_alive=300,
        # log_level=10,
    )


if __name__ == "__main__":
    # sanic sanic-app:app -p 7777 --debug --workers=2
    # or python sanic-app.py  # production-mode
    #
    # app.run(host="0.0.0.0", port=8000, debug=True, auto_reload=True)  # dev=True
    # app.run(host="0.0.0.0", port=8000, auto_reload=True)
    # dev = True

    # app.run(port=port, auto_reload=True, workers=2, debug=debug)

    # uvicorn app:app --host 0.0.0.0 --port 5555
    # curl http://127.0.0.1:5555
    # curl -XPOST http://127.0.0.1:5555/post/ -H "accept: application/json"
    # -H "Content-Type: application/json" -d "{\"text1\": \"a b c\", \"text2\": \"d e f\"}"

    app_typer()
