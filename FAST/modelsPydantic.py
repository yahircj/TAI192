from pydantic import BaseModel,Field

#Modelo de validaciones
class ModelUser(BaseModel): 
    name: str = Field(...,min_length=3,max_length=85 ,description="De 3 a 25 caracteres")
    age: int = Field(...,gt=0,lt=125, description="Edad debe ser mayor a 0")
    email: str= Field(...,example="yo@gmail.com",
                        pattern="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" ,description="12345@gmail.com")
    

class modeloAuth(BaseModel):
     email: str= Field(...,example="yo@gmail.com",
                        pattern="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" ,description="12345@gmail.com")
     passw: str = Field(..., min_length=8,strip_whitespace=True,description="Minimo 8 caracteres")