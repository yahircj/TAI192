from fastapi import FastAPI,HTTPException
from typing import Optional

app = FastAPI(
    title='Practica de api',
    description= 'Jonathan Yahir Contreras'
)

Tareas = [
{"id": 1,"titulo": "Estudiar para el examen","descripcion": "Repasar los apuntes de TAI ","vencimiento": "14-02-24", "Estado": "incompleta"},
{"id": 2,"titulo": "Autodidacta","descripcion": "Dejar de procastinar ","vencimiento": "16-02-24", "Estado": "completada"},
{"id": 3,"titulo": "Acabar videojuegos","descripcion": "Pasar la campana de death craft ll","vencimiento": "20-02-24", "Estado": "incompleta"},
{"id": 4,"titulo": "Diseñar","descripcion": "Ver tutoriales de render","vencimiento": "31-02-24", "Estado": "completada"}
]


#endpoint consulta todos
@app.get('/Alltareas', tags=['operaciones CRUD'])
def leerTareas():
    return {"Tareas: ": Tareas}

#endpoint consulta individual
@app.get('/buscarTar/{id}', tags=['operaciones CRUD'])
def encontrarTarea(id: int):
    for index, tar in enumerate(Tareas):
        if tar["id"] == id:
            return Tareas[index]
    raise HTTPException(status_code=400, detail="Id inexistente")


#endpoint Añadir
@app.post('/addtarea/', tags=['operaciones CRUD'])
def agregarTarea(tarea:dict):
    for tar in Tareas:
        if tar["id"]== tarea.get("id"):
            raise HTTPException(status_code=400, detail="Id existente")
    Tareas.append(tarea)
    return tarea


#endpoint actualizar
@app.put('/actualizarTarea/{id}', tags=['operaciones CRUD'])
def actualizarTarea(id:int, tarea:dict):
    for index,tar in enumerate(Tareas):
        if tar["id"]== id:
                Tareas[index].update(tarea)
                return Tareas(index)
    raise HTTPException(status_code=400, detail="Id inexistente")

#endpoint eliminar
@app.delete('/eliminarTarea/{id}', tags=['operaciones CRUD'])
def eliminarTarea(id: int):
    for index, tar in enumerate(Tareas):
        if tar["id"] == id:
            tarea_eliminada = Tareas.pop(index) 
            return {"Usuario eliminado usuario": tarea_eliminada}
    raise HTTPException(status_code=400, detail="Id inexistente")
