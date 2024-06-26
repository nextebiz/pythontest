from typing import Union

from fastapi import FastAPI

import uvicorn
import fastapi 

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q, 'age': 22}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)