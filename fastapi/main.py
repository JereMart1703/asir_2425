from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return ("hello world")
    

@app.get("/items/{items_id}")
def read_items(items_id: int, q: Union[str, None] = None):
    return {"items_id": items_id, "q": q}   



