from fastapi import FastAPI

app = FastAPI()

#endPoint home

@app.get('/')
def home():
    return {'hello':'world FastAPI'}

#endpoit promedio
@app.get('/promedio')
def promedio():
    return 10.5


#endpoit parametros obligatorios
@app.get('/usuario/{id}')
def consultorio(id:int):
    #caso ficticio de busqueda
    return {'Se encontro al usuario:':id}
    