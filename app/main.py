import os
from fastapi import FastAPI
from .database import engine, Base
from .routers import items
from . import models

os.makedirs("./data", exist_ok=True)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Kalmy API",
    description="""
API REST para la gestion de items
### Features
 - CRUD completo para items
 - Paginación en la lista de items
 - Validación de datos con Pydantic
 - Documentación automática con Swagger UI
 - Uso de SQLite para almacenamiento de datos
 - Testeo con Pytest automatizado con CI de GitHub Actions
 - Contenedorización con Docker
 """,
    version="1.1.0"
)

app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "API is running!"}
