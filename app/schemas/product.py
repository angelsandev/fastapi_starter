from pydantic import BaseModel, EmailStr
from typing import Optional

class ProductCreate(BaseModel):
    nombre: str
    precio: float
    correo: str
