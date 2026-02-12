from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.models.users import User
from app.schemas.users import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        username = user.username, 
        email = user.email, 
        hashed_password = hashed_password
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user