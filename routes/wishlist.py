from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user
from app.schemas.wishlist import WishlistCreate, WishlistOut
from app.crud.wishlist import create_wishlist

router = APIRouter(prefix = "/wishlist", tags=["Wishlist"])

@router.post("/", response_model=WishlistOut)
def create_new_wishlist(
    wishlist: WishlistCreate, 
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return create_wishlist(db, wishlist.title, current_user.id)