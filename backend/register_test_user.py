#!/usr/bin/env python3
"""Script para registrar un usuario de prueba"""

import requests
import json

API_URL = "http://127.0.0.1:8000"

def register_vet():
    """Registra una veterinaria de prueba"""
    print("📝 Registrando veterinaria de prueba...")
    
    data = {
        "nombre": "Veterinaria Test",
        "telefono": "8331234567",
        "direccion": "Calle Test 123",
        "email": "test@vet.com",
        "password": "test123"
    }
    
    response = requests.post(f"{API_URL}/veterinarias/registro", json=data)
    
    if response.status_code == 200:
        vet = response.json()
        print(f"✅ Veterinaria registrada!")
        print(f"   Nombre: {vet['nombre']}")
        print(f"   Email: {vet['email']}")
        print(f"   ID: {vet['id']}")
        return vet
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
        return None

if __name__ == "__main__":
    register_vet()
