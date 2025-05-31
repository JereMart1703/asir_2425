from typing import Union

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles 

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/")
def read_root():
    return ("aaaaaaa")
    
@app.get("/hola")
def hola(request : Request):
    return templates.TemplateResponse(request=request ,name="hola.html", context={"nombre": "jeremy"})
    
   
@app.get("/ejercicio2")
def pagina(request : Request):
    apellido : str = "martinez"
    edad : int = 20
    return templates.TemplateResponse(request=request ,name="pagina.html", context={"apellidos": apellido , "edad": edad})
    
   


