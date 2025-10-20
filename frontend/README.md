

# Frontend
Frontend - interfaz con React,
Aplicación frontend desarrollada en React que sirve como interfaz de usuario para interactuar con los microservicios de la plataforma.  
Permite a los usuarios autenticarse, gestionar autos, leer publicaciones del blog y recibir notificaciones.

## Funcionalidades
- Interfaz de usuario amigable e interactiva
- Conexión con Auth Service para autenticación
- Visualización y gestión de autos (Auto Service)
- Visualización de publicaciones y autores (Blog Service)
- Recepción de notificaciones por Email Service
- Compatible con dispositivos móviles y escritorio

## Tecnologías
- React.js
- Tailwind CSS / Bootstrap (según diseño)
- Axios para llamadas a APIs
- Docker / Docker Compose

## Estructura
frontend/
├── public/             # Archivos estáticos
├── src/
│   ├── components/     # Componentes reutilizables
│   ├── pages/          # Vistas de la aplicación
│   ├── services/       # Funciones para consumir APIs
│   └── utils/          # Funciones auxiliares
├── Dockerfile
└── docker-compose.yml

## Ejecución
cd frontend
docker compose up --build
Puerto por defecto: 3000

## Endpoints
La aplicación consume los siguientes servicios:
- Auth Service: `/auth/*`
- Auto Service: `/autos/*`
- Blog Service: `/posts/*`, `/authors/*`
- Email Service: `/emails/*`


