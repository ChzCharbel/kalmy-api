from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., min_length=1)
    description: str
    price: float = Field(..., gt=0)
    available: bool = True

class ItemCreate(Item):
    pass

class ItemUpdate(BaseModel):
    pass

class ItemResponse(Item):
    id: int

    class Config:
        orm_mode = True