from fastapi import FastAPI,HTTPException
from typing import Optional, List
from models import ModelUser

app = FastAPI(
    title='mi primer api',
    description= 'Jonathan Yahir Contreras',
    version='1.0.1'
)



usuarios = [
    {"id": 1, "nombre": "Alfredo", "edad": 21,"correo": "Alfredo@gmail.com"},
    {"id": 2, "nombre": "Polo", "edad": 22,"correo": "pollolin@gmail.com"},
    {"id": 3, "nombre": "Pedro", "edad": 19,"correo": "pedrsal@gmail.com"},  
    {"id": 4, "nombre": "Maria", "edad": 20,"correo": "Mariano@gmail.com"}
]

#endPoint home

@app.get('/')
def home():
    return {'hello':'world FastAPI'}

#endpoint consulta todos
@app.get('/todosUsuarios', response_model= List[ModelUser], tags=['operaciones CRUD'])
def leerUsuarios():
    return usuarios

#endpoint Añadir
@app.post('/addUsuarios/',response_model= ModelUser, tags=['operaciones CRUD'])
def agregarUsuario(usuario:ModelUser):
    for usr in usuarios:
        if usr["id"]== usuario.id:
            raise HTTPException(status_code=400, detail="Id existente")
    usuarios.append(usuario)
    return usuario

#endpoint actualizar
@app.put('/actualizarUsuarios/{id}',response_model= ModelUser, tags=['operaciones CRUD'])
def actualizarUsuario(id:int, usuarioActualizado:ModelUser):
    for index,usr in enumerate(usuarios):
        if usr["id"]== id:
                usuarios[index] = usuarioActualizado.model_dump()
                return usuarios(index)
    raise HTTPException(status_code=400, detail="Id inexistente")

#endpoint eliminar
@app.delete('/eliminarUsuario/{id}', tags=['operaciones CRUD'])
def eliminarUsuario(id: int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuario_eliminado = usuarios.pop(index) 
            return {"Usuario eliminado usuario": usuario_eliminado}
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