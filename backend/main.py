from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
import bcrypt  # <--- Usamos esto directamente en lugar de passlib
from datetime import timedelta

# IMPORTS PROPIOS
import models, schemas, auth
from database import engine, get_db

# Crear tablas
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# --- SEGURIDAD MANUAL (Sin passlib para evitar errores) ---
def get_password_hash(password):
    # Convertir a bytes, hashear y devolver como string
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd_bytes, salt).decode('utf-8')

def verify_password(plain_password, hashed_password):
    # Comparar contraseña plana con el hash guardado
    password_byte_enc = plain_password.encode('utf-8')
    hashed_password_byte_enc = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_byte_enc, hashed_password_byte_enc)

# --- CONFIGURACIÓN CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4321"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- RUTAS ---

# 1. REGISTRO
@app.post("/veterinarias/registro", response_model=schemas.VeterinariaResponse)
def registrar_veterinaria(vet: schemas.VeterinariaCreate, db: Session = Depends(get_db)):
    db_vet = db.query(models.Veterinaria).filter(models.Veterinaria.email == vet.email).first()
    if db_vet:
        raise HTTPException(status_code=400, detail="Este correo ya está registrado.")
    
    hashed_pwd = get_password_hash(vet.password)
    new_vet = models.Veterinaria(
        nombre=vet.nombre,
        telefono=vet.telefono,
        direccion=vet.direccion,
        email=vet.email,
        hashed_password=hashed_pwd
    )
    db.add(new_vet)
    db.commit()
    db.refresh(new_vet)
    return new_vet

# 2. LOGIN
@app.post("/veterinarias/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    vet = db.query(models.Veterinaria).filter(models.Veterinaria.email == form_data.username).first()
    
    # Verificación segura
    if not vet or not verify_password(form_data.password, vet.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": str(vet.id)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# --- RUTAS PROTEGIDAS ---

# 3. GET /me - Obtener información de la veterinaria autenticada
@app.get("/me", response_model=schemas.VeterinariaResponse)
def get_current_user(current_vet: models.Veterinaria = Depends(auth.get_current_veterinaria)):
    return current_vet

# 4. GET /clientes - Obtener todos los clientes de la veterinaria autenticada
@app.get("/clientes", response_model=list[schemas.ClienteResponse])
def get_clientes(
    current_vet: models.Veterinaria = Depends(auth.get_current_veterinaria),
    db: Session = Depends(get_db)
):
    # FILTRAR solo los clientes de esta veterinaria
    clientes = db.query(models.Cliente).filter(
        models.Cliente.veterinaria_id == current_vet.id
    ).all()
    return clientes

# 5. POST /clientes - Crear cliente (asignar automáticamente veterinaria_id)
@app.post("/clientes", response_model=schemas.ClienteResponse, status_code=status.HTTP_201_CREATED)
def create_cliente(
    cliente: schemas.ClienteCreate,
    current_vet: models.Veterinaria = Depends(auth.get_current_veterinaria),
    db: Session = Depends(get_db)
):
    # Crear cliente y asignar el ID de la veterinaria autenticada
    new_cliente = models.Cliente(
        **cliente.dict(),
        veterinaria_id=current_vet.id
    )
    db.add(new_cliente)
    db.commit()
    db.refresh(new_cliente)
    return new_cliente

# 6. GET /clientes/{id} - Obtener un cliente específico
@app.get("/clientes/{cliente_id}", response_model=schemas.ClienteResponse)
def get_cliente(
    cliente_id: int,
    current_vet: models.Veterinaria = Depends(auth.get_current_veterinaria),
    db: Session = Depends(get_db)
):
    cliente = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id,
        models.Cliente.veterinaria_id == current_vet.id
    ).first()
    
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    return cliente

# 7. PUT /clientes/{id} - Actualizar cliente
@app.put("/clientes/{cliente_id}", response_model=schemas.ClienteResponse)
def update_cliente(
    cliente_id: int,
    cliente_update: schemas.ClienteCreate,
    current_vet: models.Veterinaria = Depends(auth.get_current_veterinaria),
    db: Session = Depends(get_db)
):
    # Buscar el cliente y verificar que pertenece a esta veterinaria
    cliente = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id,
        models.Cliente.veterinaria_id == current_vet.id
    ).first()
    
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    # Actualizar campos
    for key, value in cliente_update.dict().items():
        setattr(cliente, key, value)
    
    db.commit()
    db.refresh(cliente)
    return cliente

# 8. DELETE /clientes/{id} - Eliminar cliente
@app.delete("/clientes/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_cliente(
    cliente_id: int,
    current_vet: models.Veterinaria = Depends(auth.get_current_veterinaria),
    db: Session = Depends(get_db)
):
    # Buscar el cliente y verificar que pertenece a esta veterinaria
    cliente = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id,
        models.Cliente.veterinaria_id == current_vet.id
    ).first()
    
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    db.delete(cliente)
    db.commit()
    return None

# 9. TEST
@app.get("/")
def read_root():
    return {"mensaje": "El Backend de Veterinaria está funcionando 🚀"}