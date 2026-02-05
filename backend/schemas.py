from pydantic import BaseModel, EmailStr
from typing import Optional

# Veterinaria Schemas
class VeterinariaCreate(BaseModel):
    nombre: str
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    email: EmailStr
    password: str

class VeterinariaResponse(BaseModel):
    id: int
    nombre: str
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    email: EmailStr

    class Config:
        from_attributes = True

# Cliente Schemas
class ClienteCreate(BaseModel):
    nombre_dueno: str
    telefono_dueno: Optional[str] = None
    email_dueno: Optional[EmailStr] = None
    direccion_dueno: Optional[str] = None
    nombre_mascota: str
    especie: str
    raza: Optional[str] = None
    edad: Optional[float] = None
    peso: Optional[float] = None
    notas: Optional[str] = None

class ClienteResponse(BaseModel):
    id: int
    nombre_dueno: str
    telefono_dueno: Optional[str]
    email_dueno: Optional[EmailStr]
    direccion_dueno: Optional[str]
    nombre_mascota: str
    especie: str
    raza: Optional[str]
    edad: Optional[float]
    peso: Optional[float]
    notas: Optional[str]
    veterinaria_id: int

    class Config:
        from_attributes = True

# Token schema
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
