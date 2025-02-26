from pydantic import BaseModel,Field

#Modelo de validaciones
class ModelUser(BaseModel): 
    id: int = Field(...,gt=0, description="id unico y solo positivos")
    nombre: str = Field(...,min_length=3,max_length=85 ,description="De 3 a 25 caracteres")
    edad: int = Field(...,gt=0,lt=125, description="Edad debe ser mayor a 0")
    correo: str= Field(...,example="yo@gmail.com",
                        pattern="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" ,description="12345@gmail.com")
    