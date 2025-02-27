import jwt

def createToken(datos:dict):
    token:str= jwt.encode(payload=datos,key='secretkay',algorithm='HS256')
    token