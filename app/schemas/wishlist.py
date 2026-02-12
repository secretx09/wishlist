from pydantic import BaseModel

class WishlistCreate(BaseModel):
    title: str

class WishlistOut(BaseModel):
    id: int
    title: str
    owner_id: int

    class Config:
        from_attributes = True