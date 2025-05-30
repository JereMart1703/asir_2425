from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return ("aaaaaaa")
    
@app.get("/hola")
def hola():
    return ("mundillo")
    
   



