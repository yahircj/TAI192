from fastapi import FastAPI

app = FastAPI()

#endPoint home

@app.get('/')
def home():
    return {'hello':'world FastAPI'}