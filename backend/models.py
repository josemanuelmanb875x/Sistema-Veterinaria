from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Veterinaria(Base):
    __tablename__ = "veterinarias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String, nullable=True)
    direccion = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    clientes = relationship("Cliente", back_populates="veterinaria", cascade="all, delete")

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre_dueno = Column(String, nullable=False)
    telefono_dueno = Column(String, nullable=True)
    email_dueno = Column(String, nullable=True)
    direccion_dueno = Column(String, nullable=True)

    nombre_mascota = Column(String, nullable=False)
    especie = Column(String, nullable=False)
    raza = Column(String, nullable=True)
    edad = Column(Float, nullable=True)
    peso = Column(Float, nullable=True)
    notas = Column(String, nullable=True)

    veterinaria_id = Column(Integer, ForeignKey("veterinarias.id"))
    veterinaria = relationship("Veterinaria", back_populates="clientes")
