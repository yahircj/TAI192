from fastapi.responses import JSONResponse
from modelsPydantic import modeloAuth
from genToken import createToken
from middlewares import BearerJWT
from fastapi import APIRouter

routerAuth = APIRouter()

@routerAuth.post('/auth',  tags=['Autenticación'])
def login(autorizacion:modeloAuth):
    if autorizacion.email == '12345a@gmail.com' and autorizacion.passw == '12345678':
        token:str = createToken(autorizacion.model_dump())
        print(token)
        return JSONResponse(content= token)
    else:
        return("Usuario no autorizado")
