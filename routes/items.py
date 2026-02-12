from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user
from app.schemas.items import ItemCreate, ItemOut, ItemUpdate
from app.models.items import Item
from app.crud.items import create_item, update_item

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("/{wishlist_id}", response_model=ItemOut)
def add_item(
    wishlist_id: int, 
    item: ItemCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return create_item(db, item, wishlist_id)

@router.get("/{item_id}", response_model=ItemOut)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.patch("/{item_id}", response_model=ItemOut)
def edit_item(
    item_id: int, 
    updates: ItemUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    item = db.query(Item).get(item_id)
    return update_item(db, item, updates)

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).get(item_id)
    db.delete(item)
    db.commit()
    return {"message": "Item deleted"}