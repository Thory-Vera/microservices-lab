# Laboratorio de Microservicios (Django + React)

## 🏗️ Arquitectura inicial

**Servicios principales:**
- `auth-service/` → Autenticación y tokens JWT  
- `blog-service/` → Publicaciones, autores y categorías  
- `email-service/` → Notificaciones y formularios  
- `frontend/` → Interfaz React  
- `reverse-proxy/` → Balanceo / Gateway local  

**Servicios base (Docker):**
- PostgreSQL → puerto **5432**
- Redis → puerto **6379**

## ⚙️ Archivos importantes
- `docker-compose.yml` → Define los servicios base (PostgreSQL y Redis)
- `.env.example` → Variables de entorno de ejemplo (base de datos y cache)
- `.env` → Variables locales (no se sube al repo)

## 🚀 Cómo iniciar el entorno
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Thory-Vera/microservices-lab.git
   cd microservices-lab
# Laboratorio de Microservicios (Django + React)

## Arquitectura inicial
- auth-service/      → Autenticación y tokens JWT
- blog-service/      → Publicaciones, autores y categorías
- email-service/     → Notificaciones y formularios
- frontend/          → Interfaz React
- reverse-proxy/     → Balanceo / Gateway local

Servicios base:
- PostgreSQL (5432)
- Redis (6379)

## Cómo levantar (rápido)
1. Copiar variables de entorno:
   ```powershell
   copy .env.example .env
