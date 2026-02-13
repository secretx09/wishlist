from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth, users,wishlist, items

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Wishlist API")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(wishlist.router)
app.include_router(items.router)