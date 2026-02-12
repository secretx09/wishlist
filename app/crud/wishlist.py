from sqlalchemy.orm import Session
from app.models.wishlist import Wishlist

def create_wishlist(db: Session, title: str, owner_id: int):
    wishlist = Wishlist(title = title, owner_id = owner_id)
    db.add(wishlist)
    db.commit()
    db.refresh(wishlist)
    return wishlist