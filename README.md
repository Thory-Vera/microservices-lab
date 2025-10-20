# 🧩 Laboratorio de Microservicios (Django + React)

## 🎯 Día 1 — Fundamentos + Entorno Docker / Git

### 👥 Objetivo general
Comprender qué es una arquitectura de microservicios y preparar el entorno de trabajo para los siguientes días.  
El grupo debe terminar el día con una base funcional en Docker Compose, donde cada servicio puede ser levantado de forma independiente.

---

## 🧠 Conceptos aprendidos
- Diferencia entre monolito y microservicios
- Principios básicos: autonomía, responsabilidad única, acoplamiento flexible, escalabilidad y observabilidad
- Estructura de proyecto “multi-servicio”
- Uso de Docker + Docker Compose para levantar contenedores
- Control de versiones en Git (ramas main y staging)

---

## ⚙️ Arquitectura inicial del proyecto
microservices-lab/
│
├── auth-service/        → Servicio de autenticación y tokens JWT
├── blog-service/        → Servicio de publicaciones, autores y categorías
├── email-service/       → Servicio de notificaciones y formularios
├── frontend/            → Interfaz React
├── reverse-proxy/       → Balanceador o gateway local
│
├── docker-compose.yml   → Configuración de Docker (PostgreSQL + Redis)
├── .env.example         → Variables de entorno del proyecto
└── README.md            → Documentación general

---

## 🐳 Servicios base (Docker)
- PostgreSQL → Puerto 5432
- Redis → Puerto 6379

Archivo docker-compose.yml:

version: "3.9"
services:
  postgres:
    image: postgres:15
    container_name: db_postgres
    restart: always
    environment:
      POSTGRES_USER: devuser
      POSTGRES_PASSWORD: devpass
      POSTGRES_DB: main_db
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  redis:
    image: redis:7
    container_name: cache_redis
    restart: always
    ports:
      - "6379:6379"

volumes:
  pgdata:

---

## 🌍 Variables de entorno
Archivo .env.example:

POSTGRES_USER=devuser
POSTGRES_PASSWORD=devpass
POSTGRES_DB=main_db
REDIS_HOST=redis
REDIS_PORT=6379

Cada integrante debe copiarlo y renombrarlo a .env localmente.

---

## 🧪 Mini-reto de cierre del día
- Levantar los contenedores con:
  docker compose up -d
  docker ps
- Crear test_connection.py (ya implementado en auth-service/) para probar conexión a PostgreSQL y Redis.

---

## ✅ Checklist del Día 1
Entregable | Descripción | Estado
----------- | ------------ | --------
🗂️ Repo Git | Subido a GitHub con estructura base y .env.example | ✅
🐳 Docker Compose | Levanta PostgreSQL y Redis sin errores | ✅
📘 README documentado | Incluye arquitectura y checklist | ✅
📸 Captura o video corto | Mostrando docker ps en ejecución | ✅

---

## 🚀 Ejecución
Para levantar todo el entorno:
docker compose up -d

Para detenerlo:
docker compose down

Para probar conexión desde el servicio de autenticación:
cd auth-service
python test_connection.py

---

## 📦 Resultado final
Entorno base de microservicios funcional con PostgreSQL y Redis listo para ampliarse con los servicios Django y React en los siguientes días.

---

✍️ Autor: Thory Milagros Vera Flores
📅 Día 1 — Laboratorio de Microservicios

