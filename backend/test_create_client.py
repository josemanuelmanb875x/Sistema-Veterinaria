#!/usr/bin/env python3
"""Script para probar la creación de clientes"""

import requests
import json

API_URL = "http://127.0.0.1:8000"

def test_login():
    """Prueba el login y retorna el token"""
    print("🔑 Probando login...")
    
    data = {
        'username': 'test@vet.com',
        'password': 'test123'
    }
    
    response = requests.post(f"{API_URL}/veterinarias/login", data=data)
    
    if response.status_code == 200:
        token = response.json()['access_token']
        print(f"✅ Login exitoso! Token: {token[:30]}...")
        return token
    else:
        print(f"❌ Error en login: {response.status_code}")
        print(response.text)
        return None

def test_create_cliente(token):
    """Prueba la creación de un cliente"""
    print("\n📝 Probando creación de cliente...")
    
    cliente = {
        "nombre_dueno": "Juan Pérez",
        "telefono_dueno": "8331234567",
        "email_dueno": "juan@test.com",
        "direccion_dueno": "Calle Principal 123",
        "nombre_mascota": "Firulais",
        "especie": "Perro",
        "raza": "Labrador",
        "edad": 3.5,
        "peso": 25.5,
        "notas": "Vacunas al día, muy juguetón"
    }
    
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    print(f"Datos a enviar: {json.dumps(cliente, indent=2, ensure_ascii=False)}")
    
    response = requests.post(f"{API_URL}/clientes", json=cliente, headers=headers)
    
    if response.status_code == 201:
        result = response.json()
        print(f"✅ Cliente creado exitosamente!")
        print(f"ID: {result['id']}")
        print(f"Dueño: {result['nombre_dueno']}")
        print(f"Mascota: {result['nombre_mascota']} ({result['especie']})")
        print(f"Edad: {result['edad']} años")
        print(f"Peso: {result['peso']} kg")
        return result
    else:
        print(f"❌ Error creando cliente: {response.status_code}")
        print(response.text)
        return None

def test_get_clientes(token):
    """Obtiene todos los clientes"""
    print("\n📋 Obteniendo lista de clientes...")
    
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(f"{API_URL}/clientes", headers=headers)
    
    if response.status_code == 200:
        clientes = response.json()
        print(f"✅ Se encontraron {len(clientes)} clientes")
        for i, c in enumerate(clientes, 1):
            print(f"  {i}. {c['nombre_mascota']} ({c['especie']}) - Dueño: {c['nombre_dueno']}")
        return clientes
    else:
        print(f"❌ Error obteniendo clientes: {response.status_code}")
        return []

if __name__ == "__main__":
    print("=" * 60)
    print("🧪 TEST DE API - SISTEMA VETERINARIA")
    print("=" * 60)
    
    # 1. Login
    token = test_login()
    if not token:
        print("\n❌ No se pudo obtener el token. Verifica las credenciales.")
        exit(1)
    
    # 2. Crear cliente
    cliente = test_create_cliente(token)
    if not cliente:
        print("\n❌ No se pudo crear el cliente.")
        exit(1)
    
    # 3. Obtener clientes
    clientes = test_get_clientes(token)
    
    print("\n" + "=" * 60)
    print("✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
    print("=" * 60)
