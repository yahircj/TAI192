from fastapi import FastAPI
from db.conexion import engine,Base
from routers.usuario import routerUsuario
from routers.auth import routerAuth



app = FastAPI(
    title='mi primer api',
    description= 'Jonathan Yahir Contreras',
    version='1.0.1'
)

app.include_router(routerUsuario)
app.include_router(routerAuth)

Base.metadata.create_all(bind=engine)


#endPoint home
@app.get('/')
def home():
    return {'hello':'world FastAPI'}
