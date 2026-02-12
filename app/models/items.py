from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    link = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
    price = Column(Float, nullable=True)

    wishlist_id = Column(Integer, ForeignKey("wishlists.id"))

    wishlist = relationship("Wishlist", back_populates="items")