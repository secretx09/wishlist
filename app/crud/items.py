from sqlalchemy.orm import Session
from app.models.items import Item
from app.schemas.items import ItemCreate, ItemUpdate

def create_item(db: Session, item: ItemCreate, wishlist_id: int):
    db_item = Item(**item.model_dump(), wishlist_id = wishlist_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, db_item: Item, updates: ItemUpdate):
    for key, value in updates.model_dump(exclude_unset = True).items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item