
Auth Service
==========================

# Auth Service

Servicio responsable de la autenticación y autorización de usuarios dentro del ecosistema de microservicios.  
Se encarga del registro, inicio de sesión y validación de tokens JWT para el acceso seguro a otros servicios.
Resumen : Auth Service - manejará autenticación y tokens
## Funcionalidades
- Registro de nuevos usuarios
- Inicio de sesión y validación de credenciales
- Generación y verificación de tokens JWT
- Middleware para proteger rutas privadas

## Tecnologías
- Python + Django REST Framework
- JWT
- Docker / Docker Compose
- Base de datos PostgreSQL

## Estructura
auth-service/
├── src/
│   ├── api/           # Rutas y serializers
│   ├── models/        # Modelos de usuario
│   ├── views/         # Lógica de endpoints
│   └── utils/         # Funciones auxiliares (JWT, validaciones)
├── manage.py
├── Dockerfile
└── docker-compose.yml

## Ejecución
cd auth-service
docker compose up --build
Puerto por defecto: 8000

## Endpoints
Método | Ruta           | Descripción
-------|----------------|-----------------------------
POST   | /auth/register | Crear un nuevo usuario
POST   | /auth/login    | Iniciar sesión
GET    | /auth/verify   | Verificar token JWT


Auto Service
==========================

# Auto Service

Servicio encargado de la gestión de autos dentro de la plataforma.  
Permite crear, actualizar, eliminar y consultar autos, asegurando la integración con otros microservicios.

## Funcionalidades
- Gestión completa de autos (CRUD)
- Integración con Auth Service para usuarios autenticados
- API REST escalable y mantenible

## Tecnologías
- Python + Django REST Framework
- Docker / Docker Compose
- Base de datos PostgreSQL

## Estructura
auto-service/
├── src/
│   ├── api/           # Rutas y serializers
│   ├── models/        # Modelos de autos
│   ├── views/         # Lógica de endpoints
│   └── utils/         # Funciones auxiliares
├── manage.py
├── Dockerfile
└── docker-compose.yml

## Ejecución
cd auto-service
docker compose up --build
Puerto por defecto: 8001

## Endpoints
Método | Ruta           | Descripción
-------|----------------|-----------------------------
GET    | /autos/        | Listar todos los autos
POST   | /autos/        | Crear un nuevo auto
GET    | /autos/{id}/   | Obtener detalles de un auto
PUT    | /autos/{id}/   | Actualizar un auto
DELETE | /autos/{id}/   | Eliminar un auto



