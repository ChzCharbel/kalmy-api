from pydantic import BaseModel, Field, typing
from pydantic import ConfigDict
from typing import Optional

class Item(BaseModel):
    name: str = Field(..., min_length=1, description="Nombre del item", example="Laptop")
    description: str = Field(..., min_length=1, description="Descripción del item", example="Laptop Gamer")
    price: float = Field(..., gt=0, description="Precio del item", example=1500.00)
    available: bool = Field(default=True, description="Disponibilidad del item", example=True)

class ItemCreate(Item):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = Field(default=None, description="Nombre del item", example="Updated Laptop")
    description: Optional[str] = Field(default=None, description="Descripción del item", example="Updated Laptop Gamer")
    price: Optional[float] = Field(default=None, gt=0, description="Precio del item", example=1400.00)
    available: Optional[bool] = Field(default=None, description="Disponibilidad del item", example=False)

class ItemResponse(Item):
    id: int

    model_config = ConfigDict(from_attributes=True)