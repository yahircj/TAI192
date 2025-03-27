from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from modelsPydantic import ModelUser, modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from db.conexion import session
from models.modelsDB import User
from fastapi import APIRouter

routerUsuario = APIRouter()



#endpoint consulta todos
@routerUsuario.get('/todosUsuarios', tags=['operaciones CRUD'])
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
@routerUsuario.get('/usuario/{id}', tags=['operaciones CRUD'])
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
@routerUsuario.post('/addUsuarios/', response_model=ModelUser, tags=['operaciones CRUD'])
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



# Endpoint actualizar
@routerUsuario.put('/actualizarUsuarios/{id}', response_model=ModelUser, tags=['operaciones CRUD'])
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
@routerUsuario.delete('/eliminarUsuario/{id}', tags=['operaciones CRUD'])
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

