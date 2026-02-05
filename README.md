# 🏥 Sistema de Gestión Veterinaria

Sistema completo para la gestión de clientes y mascotas en clínicas veterinarias, con autenticación JWT, dashboard interactivo y validaciones en tiempo real.

![Veterinaria](https://img.shields.io/badge/Status-Activo-success)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Astro](https://img.shields.io/badge/Astro-5.17-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-0.128-green)

## 🚀 Características

- ✅ **Autenticación segura** con JWT (JSON Web Tokens)
- 👥 **Gestión completa de clientes** (CRUD)
- 🐾 **Registro detallado de mascotas** (edad, peso, raza, notas)
- 📊 **Dashboard con KPIs** (Total clientes, Perros, Gatos)
- 🎨 **Diseño moderno** con Glassmorphism y gradientes
- ✅ **Validaciones en tiempo real** 
  - Teléfono: 10 dígitos obligatorios
  - Email: dominios válidos (gmail, outlook, hotmail, etc.)
  - Edad: 0-50 años con decimales
  - Peso: 0.1-200 kg con decimales
- 📱 **Interfaz responsive**

## 🛠️ Tecnologías

### Backend
- **FastAPI** - Framework web de alto rendimiento
- **SQLAlchemy** - ORM para base de datos
- **SQLite** - Base de datos
- **python-jose** - Manejo de JWT
- **bcrypt** - Hash de contraseñas
- **Pydantic** - Validación de datos

### Frontend
- **Astro** - Framework web moderno
- **Tailwind CSS** - Estilos utility-first
- **JavaScript** - Vanilla JS (sin frameworks pesados)

## 📦 Instalación

### Requisitos
- Python 3.9+
- Node.js 18+

### 1. Clonar repositorio
```bash
git clone https://github.com/TU_USUARIO/veterinaria.git
cd veterinaria
```

### 2. Instalar dependencias Backend
```bash
cd backend
pip install fastapi sqlalchemy python-jose bcrypt uvicorn passlib
```

### 3. Inicializar base de datos con datos de prueba
```bash
python reiniciar_db.py
```

### 4. Instalar dependencias Frontend
```bash
cd ..
npm install
```

### 5. Iniciar proyecto

**Opción A: Script automático (Windows)**
```powershell
.\iniciar_proyecto.ps1
```

**Opción B: Manual (2 terminales)**

Terminal 1 - Backend:
```bash
cd backend
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Terminal 2 - Frontend:
```bash
npm run dev
```

### 6. Abrir aplicación
- **Frontend**: http://localhost:4321
- **API Docs**: http://127.0.0.1:8000/docs

## 🔑 Credenciales de Prueba

```
Email: test@vet.com
Contraseña: test123
```

## 📁 Estructura del Proyecto

```
veterinaria/
├── backend/
│   ├── main.py              # API endpoints
│   ├── models.py            # Modelos SQLAlchemy
│   ├── schemas.py           # Esquemas Pydantic
│   ├── auth.py              # Autenticación JWT
│   ├── database.py          # Configuración DB
│   └── reiniciar_db.py      # Script inicialización
├── src/
│   ├── pages/
│   │   ├── index.astro      # Login
│   │   ├── registro.astro   # Registro
│   │   └── dashboard.astro  # Dashboard
│   └── services/            # Servicios API
└── iniciar_proyecto.ps1     # Script inicio automático
```

## 📊 API Endpoints

### Autenticación
- `POST /veterinarias/registro` - Registrar veterinaria
- `POST /veterinarias/login` - Iniciar sesión
- `GET /veterinarias/me` - Info usuario actual

### Clientes
- `GET /clientes` - Listar clientes
- `POST /clientes` - Crear cliente
- `PUT /clientes/{id}` - Actualizar cliente
- `DELETE /clientes/{id}` - Eliminar cliente

## 🔐 Seguridad

- ✅ Contraseñas hasheadas con bcrypt
- ✅ Autenticación JWT
- ✅ Validación frontend y backend
- ✅ Protección de rutas
- ✅ Filtrado por veterinaria

## 🚀 Despliegue

### Backend
Recomendado: Railway, Render, Heroku
> Cambiar SQLite por PostgreSQL en producción

### Frontend
Recomendado: Vercel, Netlify, Cloudflare Pages

## 👨‍💻 Autor

**[Tu Nombre]**
- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- LinkedIn: [tu-perfil](https://linkedin.com/in/tu-perfil)

---

⭐ Si te gustó este proyecto, dale una estrella!

El servidor quedará en `http://127.0.0.1:8000`.

## Frontend — instalar y ejecutar

Desde la raíz del proyecto (donde está `package.json`):

```bash
npm install
npm run dev
```

El frontend por defecto de Astro suele correr en `http://localhost:4321` (según tu config).

## Endpoints principales (Backend)

- `POST /register` — Registrar una nueva veterinaria.
  - Body (JSON): `nombre`, `telefono`, `direccion`, `email`, `password`.
  - Respuesta: `VeterinariaResponse` (sin password).

- `POST /login` — Login (OAuth2 form data).
  - Envío: `application/x-www-form-urlencoded` con `username` (email) y `password`.
  - Respuesta: `{ "access_token": "<token>", "token_type": "bearer" }`.

- `GET /me` — Devuelve la veterinaria autenticada. Header: `Authorization: Bearer <token>`.

- `GET /clientes` — Lista clientes de la veterinaria autenticada.
- `POST /clientes` — Crear cliente (se asigna `veterinaria_id` automáticamente).
- `GET /clientes/{id}` — Obtener cliente (solo si pertenece a la veterinaria).
- `PUT /clientes/{id}` — Actualizar cliente (validación de pertenencia).
- `DELETE /clientes/{id}` — Eliminar cliente (validación de pertenencia).

Todos los endpoints de clientes requieren el header `Authorization: Bearer <token>`.

## Notas sobre autenticación y tokens

- El login devuelve un JWT firmado (configurado en `backend/auth.py`). El frontend guarda el token en `localStorage` como `token`.
- El frontend envía `Authorization: Bearer <token>` en llamadas protegidas (`/me`, `/clientes`, etc.).

## CORS

CORS está configurado para permitir `http://localhost:4321` en `backend/main.py`.

## Archivos clave a revisar

- `backend/schemas.py` — Esquemas Pydantic (Create / Response).
- `backend/models.py` — Modelos SQLAlchemy (`Veterinaria`, `Cliente`).
- `backend/auth.py` — Hashing con `passlib` y JWT (`python-jose`).
- `src/services/auth.ts` — Funciones `register`, `login`, `getToken`, `logout`.
- `src/services/clientes.ts` — Funciones para CRUD de clientes con token.

## Ejemplo rápido (login desde curl)

```bash
curl -X POST "http://127.0.0.1:8000/login" -H "Content-Type: application/x-www-form-urlencoded" -d "username=tu@email.com&password=tu_pass"
```

## Siguientes pasos sugeridos

- Ejecutar el backend y verificar los endpoints con `curl` o Postman.
- Iniciar el frontend y probar el flujo: registro → login → dashboard → CRUD clientes.

Si quieres, puedo:

- Ejecutar el servidor aquí para hacer pruebas automáticas (necesito permiso).
- Generar colecciones de Postman / ejemplos de requests más detallados.

---

Archivo generado automáticamente: `README.md` — versión inicial.
