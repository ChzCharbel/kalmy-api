# Kalmy Items API

API REST desarrollada con **FastAPI** para la gestión de un recurso `Item`.  
El proyecto fue construido como parte de un proceso técnico, priorizando buenas
prácticas de desarrollo backend: diseño de APIs, validaciones, persistencia,
testing automatizado, CI/CD y contenedorización.

---

##  Cómo correr la API

### Opción 1: Ejecutar localmente (Python)

#### 1. Clonar el repositorio
```bash
git clone <repo-url>
cd kalmy-api
```

#### 2. Crear y activar entorno virtual

```bash
python -m venv venv
source venv/bin/activate   
# Windows: venv\Scripts\activate
```

#### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

#### 4. Ejecutar la aplicación

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:

- http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

### Opción 2: Ejecutar con Docker (recomendado)

#### 1. Construir la imagen

```bash
docker build -t kalmy-api .
```

#### 2. Correr el contenedor con persistencia de datos

```bash
docker run -p 8000:8000 -v $(pwd)/data:/app/data kalmy-api
```

En Windows (PowerShell):

```bash
docker run -p 8000:8000 -v ${PWD}/data:/app/data kalmy-api
```

Acceder a:

- http://localhost:8000
- http://localhost:8000/docs

La base de datos SQLite se persiste usando un volumen Docker.

## 🧠 Decisiones tecnológicas y justificación

### FastAPI

- Framework moderno y rápido basado en ASGI.
- Genera documentación automática con OpenAPI/Swagger.
- Facilita validaciones y tipado estricto.

### SQLAlchemy + SQLite

- SQLAlchemy permite separar la lógica de negocio del acceso a datos.
- SQLite se eligió por simplicidad y rapidez de setup.
- La arquitectura permite migrar fácilmente a PostgreSQL u otro motor.

### Pydantic v2

- Validación estricta de datos de entrada y salida.
- Separación clara entre modelos de base de datos y contratos de la API.
- Uso de configuración moderna (ConfigDict).

### Separación por capas

El proyecto está organizado en capas claras:

- **models**: modelos de base de datos
- **schemas**: validaciones y contratos de la API
- **crud**: lógica de negocio
- **routers**: endpoints HTTP

Esto mejora mantenibilidad, escalabilidad y testeo.

### Paginación

- El endpoint GET /items implementa skip y limit.
- Evita devolver grandes volúmenes de datos.
- Representa una buena práctica en APIs de producción.

## 📚 Endpoints disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | /items | Lista items (con paginación) |
| GET | /items/{id} | Obtener item por ID |
| POST | /items | Crear un item |
| PUT | /items/{id} | Actualizar un item |
| DELETE | /items/{id} | Eliminar un item |

### Ejemplo de paginación

```
GET /items?skip=0&limit=10
```

## 🧪 Cómo probar los endpoints

### 1️⃣ Usando Swagger UI

Accede a:

http://127.0.0.1:8000/docs

Desde ahí puedes:

- Crear items
- Listarlos con paginación
- Actualizarlos y eliminarlos
- Ver validaciones y errores HTTP

### 2️⃣ Tests automatizados (pytest)

El proyecto incluye tests automatizados que cubren:

- Creación de items
- Listado
- Actualización (PUT)
- Manejo de errores (404)
- Paginación

Ejecutar tests:

```bash
pytest
```

### 3️⃣ CI/CD con GitHub Actions

El repositorio incluye un workflow de GitHub Actions que:

- Se ejecuta en cada push y pull request
- Instala dependencias
- Ejecuta los tests automáticamente
- Falla si algún test no pasa

Esto garantiza calidad continua y evita regresiones.

## 🧪 Flujo de desarrollo del proyecto

1. Desarrollo local
2. Tests automatizados con pytest
3. Validación automática con GitHub Actions
4. Ejecución reproducible con Docker
