import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import base64
import numpy as np
import sys
from io import StringIO
from pydantic import BaseModel
from typing import Optional
import time
import os

app = FastAPI()
db = {"tasks":{}, "data":{}}


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


class Image(BaseModel):
    fingerprint: str
    dtype: str
    shape: tuple
    data: str

    def deserialize(self):
        q = np.frombuffer(base64.decodebytes(eval(self.data)), dtype=eval(f"np.{self.dtype}"))
        return q.reshape(self.shape)


class Task(BaseModel):
    module: str
    function: str
    args: list
    kwargs: dict
    meta: Optional[dict]
    result: Optional[str]
    logger: Optional[list]



@app.get("/", response_class=JSONResponse)
async def get():
    return {
        os.getpid(): {
            "tasks": list(db["tasks"].keys()),
            "data": list(db["data"].keys())
        }}


@app.get("/tasks/{id}", response_class=JSONResponse)
def get(id:str):
    while not id in db["tasks"]:
        time.sleep(1)
    return db["tasks"][id]

@app.post("/tasks/{id}", response_class=JSONResponse)
async def index(id:str, task: Task):
    def reference(v):
        if type(v)==str and v[:8]=="zakuro::":
            return db['data'][v]
    # Doing
    _args = task.args
    _kwargs = dict([(k, reference(v)) for k, v in task.kwargs.items()])
    commands =[
        f"from {task.module} import {task.function}",
        "with Capturing() as task.logger: " \
        f"    task.result = {task.function}(*_args, **_kwargs)"
    ]
    for command in commands:
        print(command)
        exec(command)
    task = task.dict()
    db["tasks"][id] = task
    return {"success": True}


@app.post("/data/{fingerprint}", response_class=JSONResponse)
def store(fingerprint:str, image: Image):
    db["data"][fingerprint] = image.deserialize()
    return {"state": "serialized"}


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('port', metavar='N', type=int, default=9000)
    args = parser.parse_args()
    uvicorn.run(app, host="0.0.0.0", port=args.port)