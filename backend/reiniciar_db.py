"""
Script para reinicializar la base de datos con datos de prueba
"""
import os
import bcrypt
from database import engine, SessionLocal
from models import Base, Veterinaria, Cliente

def get_password_hash_simple(password: str) -> str:
    """Hashea una contraseña usando bcrypt directamente"""
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd_bytes, salt)
    return hashed.decode('utf-8')

def reiniciar_database():
    # Eliminar base de datos si existe
    db_path = "veterinaria.db"
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"✅ Base de datos eliminada: {db_path}")
    
    # Crear todas las tablas
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas correctamente")
    
    # Crear sesión
    db = SessionLocal()
    
    try:
        # Crear veterinaria de prueba
        password = "test123"
        hashed = get_password_hash_simple(password)
        vet_test = Veterinaria(
            nombre="Veterinaria Test",
            telefono="8331234567",
            direccion="Av. Principal #123, Centro",
            email="test@vet.com",
            hashed_password=hashed
        )
        db.add(vet_test)
        db.commit()
        db.refresh(vet_test)
        print(f"✅ Veterinaria creada: {vet_test.email} (ID: {vet_test.id})")
        
        # Crear cliente de prueba
        cliente_test = Cliente(
            nombre_dueno="Juan Pérez",
            telefono_dueno="8331234567",
            email_dueno="juan@test.com",
            direccion_dueno="Calle Secundaria #456",
            nombre_mascota="Firulais",
            especie="Perro",
            raza="Labrador",
            edad=3.5,
            peso=25.5,
            notas="Vacunas al día, muy juguetón",
            veterinaria_id=vet_test.id
        )
        db.add(cliente_test)
        db.commit()
        db.refresh(cliente_test)
        print(f"✅ Cliente creado: {cliente_test.nombre_dueno} con mascota {cliente_test.nombre_mascota} (ID: {cliente_test.id})")
        
        print("\n" + "="*60)
        print("🎉 BASE DE DATOS REINICIALIZADA CORRECTAMENTE")
        print("="*60)
        print("\n📋 CREDENCIALES DE ACCESO:")
        print(f"   Email: test@vet.com")
        print(f"   Contraseña: test123")
        print("\n👤 DATOS DE PRUEBA:")
        print(f"   Veterinaria: {vet_test.nombre}")
        print(f"   Cliente: {cliente_test.nombre_dueno}")
        print(f"   Mascota: {cliente_test.nombre_mascota} ({cliente_test.especie})")
        print(f"   Edad: {cliente_test.edad} años")
        print(f"   Peso: {cliente_test.peso} kg")
        print("="*60)
        
    except Exception as e:
        print(f"❌ Error al crear datos: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    reiniciar_database()
