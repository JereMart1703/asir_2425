from data.database import database
from typing import Annotated

from data.dao.dao_alumnos import DaoAlumnos

from data.modelo.menu import Menu

from typing import Union

from fastapi import FastAPI, Request,Form



from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="./static"), name="static")


templates = Jinja2Templates(directory="templates")



@app.get("/")
def read_root(request: Request):
    menu = Menu(True,False)
    return templates.TemplateResponse(
    request=request, name="index.html",context={"menu": menu})
    

@app.get("/alumnos")
def get_alumnos(request: Request,nombre : str = "pepe",otro: int  = 1):

    menu = Menu(True,True)
    alumnos =  DaoAlumnos().get_all(database)
   

    return templates.TemplateResponse(
    request=request, name="alumnos.html", context={"menu": menu,"alumnos": alumnos,"nombre": nombre} )
   
   

@app.get("/deletealumnos/{alumno_id}")
def delete_alumnos(request: Request,alumno_id:str):
    dao = DaoAlumnos()
    dao.delete(database, alumno_id)
    
    alumnos =  dao.get_all(database)
    return templates.TemplateResponse(
    request=request, name="alumnos.html", context={"alumnos": alumnos}                                                      
)

  

@app.post("/delalumnos")
def del_alumnos(request: Request,alumno_id:Annotated[str, Form()] ):
    print("hlhl")
    dao = DaoAlumnos()
    dao.delete(database, alumno_id)
    
    alumnos =  dao.get_all(database)
    return templates.TemplateResponse(
    request=request, name="alumnos.html", context={"alumnos": alumnos} )

@app.get("/formaddalumnos")
def form_add_alumnos(request: Request):
    return templates.TemplateResponse(
    request=request, name="formaddAlumnos.html"
    )

@app.post("/addalumnos")
def add_alumnos(request: Request, nombre: Annotated[str, Form()] = None):
    if nombre is None:
        return templates.TemplateResponse(
        request=request, name="alumnos.html", context={"nombre": "pepe"}
        )
    
    dao = DaoAlumnos()
    dao.insert(database, nombre)
    
    alumnos =  dao.get_all(database)
    return templates.TemplateResponse(
    request=request, name="formaddAlumnos.html", context={"alumnos": alumnos}                                                      
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



