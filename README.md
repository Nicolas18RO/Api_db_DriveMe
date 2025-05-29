# DRIVEME - DOCUMENTACIÓN DEL SISTEMA

Plataforma que conecta conductores y usuarios mediante una API RESTful desarrollada con Django y PostgreSQL.

## CARACTERÍSTICAS PRINCIPALES

### GESTIÓN DE CONDUCTORES
    Registro y verificación de documentos
    Validación de licencias
    Historial de viajes completados

### GESTIÓN DE USUARIOS
    Registro con verificación de email
    Métodos de pago integrados
    Sistema de calificaciones

### OPERACIONES DE VIAJE
    Solicitud en tiempo real
    Seguimiento GPS activo
    Sistema de tarifas dinámicas
    Notificaciones push

## TECNOLOGÍAS IMPLEMENTADAS

### BACKEND (API)
    DJANGO (Framework principal)
    DJANGO REST FRAMEWORK (Para construcción de API REST)
    PSYCOPG2 (Adaptador para PostgreSQL)

### BASE DE DATOS
    POSTGRESQL (Sistema de gestión de base de datos relacional)

## INSTALACIÓN Y CONFIGURACIÓN

### REQUISITOS PREVIOS
    Python 3.10+ (python --version)
    PostgreSQL 14+ (psql --version)
    pip (Gestor de paquetes de Python)
    Git (Opcional, para clonar el repositorio)

### PASOS A SEGUIR:
1. CONFIGURAR ENTORNO
    Clonar repositorio: https://github.com/Nicolas18RO/Api_db_DriveMe/tree/main

2. Crear y activar entorno virtual:
    python -m venv venv
    venv\Scripts\activate

3.  INSTALAR DEPENDENCIAS
Django (pip install Django)
    Versión recomendada: 4.2+
    Función: Framework web principal
    Uso en DriveMe:
    Estructura MVC del proyecto
    Sistema de rutas URL
    Panel de administración automático
    ORM para modelos de base de datos

djangorestframework (pip install djangorestframework)
    Versión recomendada: 3.14+
    Función: Construcción de API REST
    Uso en DriveMe:
    Creación de endpoints para:
        /api/drivers/
        /api/trips/
         /api/customers/
    Serialización de modelos a JSON
    Autenticación API

psycopg (pip install psycopg)
    Versión recomendada: 3.1+
    Función: Adaptador PostgreSQL para Python
    Uso en DriveMe:
    Conexión entre Django y PostgreSQL
    Ejecución eficiente de consultas
    Soporte para tipos de datos geográficos (ubicaciones)

django-filter (pip install django-filter)
    Versión recomendada: 2.4+
    Función: Sistema de filtrado avanzado
    Uso en DriveMe:
    Filtrado de conductores por:
    Disponibilidad
    Tipo de vehículo
    Ubicación
    Búsqueda de viajes por estado
    Filtros complejos en listados

python-decouple (pip install python-decouple)
    Versión recomendada: 3.8+
    Función: Gestión de configuraciones
    Uso en DriveMe:
    Manejo seguro de:
    Claves secretas
    Credenciales de DB
    Configuraciones de entorno
    Separación entre configs de desarrollo/producción

django-cors-headers (pip install django-cors-headers)
    Versión recomendada: 3.13+
    Función: Manejo de CORS (Cross-Origin)
    Uso en DriveMe:
    Permitir conexiones desde:
    Aplicación móvil
    Frontend web (React/Vue)

4. Crear base de datos en PostgreSQL

5. Modificar archivo .env en la raíz del proyecto:

    ENGINE=django.db.backends.postgresql
    NAME=nombre de tu base de datos credada en PostgresSQL
    USER=postgres
    PASSWORD=Tucontraseña
    HOST=localhost
    PORT=5432

