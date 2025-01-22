from data.database import database
from typing import Annotated

from data.dao.dao_alumnos import DaoAlumnos

from typing import Union

from fastapi import FastAPI, Request,Form



from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")


templates = Jinja2Templates(directory="templates")



@app.get("/")
def read_root():
    return DaoAlumnos().get_all(database)
    

@app.get("/alumnos/{alumno_id}")
def get_alumnos(request: Request,alumno_id:str,nombre : str = "pepe",otro: int  = 1):
    alumnos =  DaoAlumnos().get_all(database)
   

    return templates.TemplateResponse(
    request=request, name="alumnos.html", context={"alumnos": alumnos,"nombre": nombre}                                                      
)
   
   

@app.get("/deletealumnos/{alumno_id}")
def delete_alumnos(request: Request,alumno_id:str):
    dao = DaoAlumnos()
    dao.delete(database, alumno_id)
    
    alumnos =  dao.get_all(database)
    return templates.TemplateResponse(
    request=request, name="alumnos.html", context={"alumnos": alumnos}                                                      
)

@app.post("/addalumnos")
@app.get("/addalumnos")
def add_alumnos(request: Request, nombre: Annotated[str, Form()] = None):
    if nombre is None:
        return templates.TemplateResponse(
        request=request, name="alumnos.html", context={"nombre": "pepe"}
        )
    
    dao = DaoAlumnos()
    dao.insert(database, nombre)
    
    alumnos =  dao.get_all(database)
    return templates.TemplateResponse(
    request=request, name="alumnos.html", context={"alumnos": alumnos}                                                      
)    

@app.get("/test", response_class=HTMLResponse)
async def test(request: Request):
    
   
    return templates.TemplateResponse(
        request=request, name="index.html", context={"nombre": "pepe"}                                                      
    )

@app.get("/items", response_class=HTMLResponse)
async def read_item(request: Request):
    
    students = [ {"nombre": "pepe", "edad": 20,"score": 50}, {"nombre": "pepe", "edad": 20,"score": 50}, {"nombre": "pepe", "edad": 20,"score": 90}]
    return templates.TemplateResponse(
        request=request, name="students.html", context={"nombre": "pepe","students": students}                                                      
    )



