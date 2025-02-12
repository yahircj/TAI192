from fastapi import FastAPI,HTTPException
from typing import Optional

app = FastAPI(
    title='mi primer api',
    description= 'Jonathan Yahir Contreras',
    version='1.0.1'
)

usuarios = [
    {"id": 1, "nombre": "Alfredo", "edad": 21},
    {"id": 2, "nombre": "Polo", "edad": 22},
    {"id": 3, "nombre": "Pedro", "edad": 19},  
    {"id": 4, "nombre": "Maria", "edad": 20}
]

#endPoint home

@app.get('/')
def home():
    return {'hello':'world FastAPI'}

#endpoint consulta todos
@app.get('/todosUsuarios', tags=['operaciones CRUD'])
def leerUsuarios():
    return {"Los usuarios registrados son: ": usuarios}

#endpoint consulta todos
@app.post('/addUsuarios/', tags=['operaciones CRUD'])
def agregarUsuario(usuario:dict):
    for usr in usuarios:
        if usr["id"]== usuario.get("id"):
            raise HTTPException(status_code=400, detail="Id existente")
    usuarios.append(usuario)
    return usuario

@app.put('/actualizarUsuarios/{id}', tags=['operaciones CRUD'])
def actualizarUsuario(id:int, usuario:dict):
    for index,usr in enumerate(usuarios):
        if usr["id"]== id:
                usuarios[index].update(usuario)
                return usuarios(index)
    raise HTTPException(status_code=400, detail="Id inexistente")



""" #endpoit promedio
@app.get('/promedio')
def promedio():
    return 10.5


#endpoit parametros obligatorios
@app.get('/usuario/{id}',tags= ['obligatorio'])
def consultorio(id:int):
    #caso ficticio de busqueda
    return {'Se encontro al usuario:':id}
    

#endpoit parametros opcional
@app.get('/usuario/',tags= ['Parametro opcional'])
def consultorioop(id:Optional[int]=None):
    #caso ficticio de busqueda
    if id is not None:
        for usu in usuarios:
            if usu['id'] == id:
                return {"MENSAJE":"Usuario encontrado:", "usuario": usu}
        return {'mensaje':f'usuario:{id} no encontrado'}
    return{'mensaje':'No hay id'}


#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (id is None or usuario["id"] == id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."} """