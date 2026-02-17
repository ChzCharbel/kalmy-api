from pydantic import BaseModel, Field, typing
from pydantic import ConfigDict
from typing import Optional

class Item(BaseModel):
    name: str = Field(..., min_length=1)
    description: str
    price: float = Field(..., gt=0)
    available: bool = True

class ItemCreate(Item):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    available: Optional[bool] = None

class ItemResponse(Item):
    id: int

    model_config = ConfigDict(from_attributes=True)