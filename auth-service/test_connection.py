import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auth_service.settings')
django.setup()

from django.db import connection

try:
    connection.ensure_connection()
    print("✅ Conexión a la base de datos exitosa.")
except Exception as e:
    print("❌ Error al conectar con la base de datos:", e)
