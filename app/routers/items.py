from fastapi import APIRouter, Depends, HTTPException, status, Query, Body
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter(
    prefix="/items",
    tags=["items"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get(
    "/",
    response_model=list[schemas.ItemResponse],
    summary="Lista de Items",
    description="Devuelve una lista de items con paginación."
)
def list_items(
    skip: int = Query(0, ge=0, description="Número de items a saltar"),
    limit: int = Query(10, ge=1, le=100, description="Número de items a devolver"),
    db: Session = Depends(get_db)
):
    return crud.get_items(db, skip=skip, limit=limit)


@router.get(
    "/{item_id}",
    response_model=schemas.ItemResponse,
    summary="Obtener Item por ID",
    description="Devuelve un item específico por su ID."
)
def get_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return item


@router.post(
    "/",
    response_model=schemas.ItemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear Item",
    description="Crea un nuevo item.",
    responses={
        201: {
            "description": "Item creado exitosamente",
            "content": {
                "application/json": {
                    "example": {
                        "name": "Laptop",
                        "description": "Laptop Gamer",
                        "price": 1500.00,
                        "available": True
                    }
                }
            }
        },
        400: {"description": "Solicitud inválida"}
    }
)
def create_item(
    item: schemas.ItemCreate,
    db: Session = Depends(get_db)
):
    return crud.create_item(db, item)


@router.put(
    "/{item_id}",
    response_model=schemas.ItemResponse,
    summary="Actualizar Item",
    description="Actualiza un item existente por su ID."
)
def update_item(
    item_id: int,
    item: schemas.ItemUpdate = Body(...),
    db: Session = Depends(get_db)
):
    updated_item = crud.update_item(db, item_id, item)
    if not updated_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return updated_item


@router.delete(
    "/{item_id}",
    response_model=schemas.ItemResponse,
    summary="Eliminar Item",
    description="Elimina un item por su ID."
)
def delete_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    deleted_item = crud.delete_item(db, item_id)
    if not deleted_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    return deleted_item
