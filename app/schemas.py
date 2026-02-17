from pydantic import BaseModel, Field, typing
from pydantic import ConfigDict
from typing import Optional

class Item(BaseModel):
    name: str = Field(..., min_length=1, description="Nombre del item")
    description: str = Field(..., min_length=1, description="Descripción del item")
    price: float = Field(..., gt=0, description="Precio del item")
    available: bool = Field(default=True, description="Disponibilidad del item")

class ItemCreate(Item):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = Field(default=None, description="Nombre del item")
    description: Optional[str] = Field(default=None, description="Descripción del item")
    price: Optional[float] = Field(default=None, gt=0, description="Precio del item")
    available: Optional[bool] = Field(default=None, description="Disponibilidad del item")
class ItemResponse(Item):
    id: int

    model_config = ConfigDict(from_attributes=True)