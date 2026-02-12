from pydantic import BaseModel
from typing import Optional

class ItemCreate(BaseModel):
    name: str
    link: str
    image_url: str
    price: Optional[float] = None

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None

class ItemOut(BaseModel):
    id: int
    name: str
    link: str
    image_url: str
    price: Optional[float]
    wishlist_id: int

    class Config:
        from_attributes = True