from fastapi import FastAPI,HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List
from modelsPydantic import ModelUser, modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from db.conexion import session,engine,Base
from models.modelsDB import User

app = FastAPI(
    title='mi primer api',
    description= 'Jonathan Yahir Contreras',
    version='1.0.1'
)

Base.metadata.create_all(bind=engine)

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
@app.get('/todosUsuarios', tags=['operaciones CRUD'])
def leerUsuarios():
    db = session()
    try:
        consulta= db.query(User).all()
        return JSONResponse(content= jsonable_encoder(consulta))
    
    except Exception as e:
        return JSONResponse(status_code=500,
                            content={"message": "Error al consultar",
                                     "Excepcion": str(e)}) 
    finally:
        db.close


#buscar 1
#endpoint consulta todos
@app.get('/usuario/{id}', tags=['operaciones CRUD'])
def buscarusuario(id:int):
    db = session()
    try:
        consulta= db.query(User).filter(User.id == id).first()
        if not consulta:
             return JSONResponse(content= jsonable_encoder(consulta))
        
        return JSONResponse(content= jsonable_encoder(consulta))
       
    
    except Exception as e:
        return JSONResponse(status_code=500,
                            content={"message": "Error al consultar",
                                     "Excepcion": str(e)}) 
    finally:
        db.close

#endpoint Añadir
@app.post('/addUsuarios/', response_model=ModelUser, tags=['operaciones CRUD'])
def agregarUsuario(usuario: ModelUser):
    db = session()
    try:
        db.add(User(**usuario.model_dump()))
        db.commit()  
        return JSONResponse(status_code=201,
                            content={"message": "Usuario Guardado",
                                     "usuario": usuario.model_dump()}) 
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"message": "Error al guardar usuario",
                                     "Excepcion": str(e)}) 
    finally:
        db.close()


@app.post('/auth',  tags=['Autenticación'])
def login(autorizacion:modeloAuth):
    if autorizacion.email == '12345a@gmail.com' and autorizacion.passw == '12345678':
        token:str = createToken(autorizacion.model_dump())
        print(token)
        return JSONResponse(content= token)
    else:
        return("Usuario no autorizado")

# Endpoint actualizar
@app.put('/actualizarUsuarios/{id}', response_model=ModelUser, tags=['operaciones CRUD'])
def actualizarUsuario(id: int, usuarioActualizado: ModelUser):
    db = session()
    try:
        usuario = db.query(User).filter(User.id == id).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        for key, value in usuarioActualizado.model_dump().items():
            setattr(usuario, key, value)
        
        db.commit()
        return JSONResponse(status_code=200, content={"message": "Usuario actualizado", "usuario": jsonable_encoder(usuario)})
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail={"message": "Error al actualizar usuario", "Excepcion": str(e)})
    finally:
        db.close()

# Endpoint eliminar
@app.delete('/eliminarUsuario/{id}', tags=['operaciones CRUD'])
def eliminarUsuario(id: int):
    db = session()
    try:
        usuario = db.query(User).filter(User.id == id).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        db.delete(usuario)
        db.commit()
        return JSONResponse(status_code=200, content={"message": "Usuario eliminado"})
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail={"message": "Error al eliminar usuario", "Excepcion": str(e)})
    finally:
        db.close()



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