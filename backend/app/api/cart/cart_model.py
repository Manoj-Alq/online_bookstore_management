from configuration.config import *
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, ARRAY
from sqlalchemy.orm import relationship

class Cart(Base):
    __tablename__ = "cart"

    cart_id = Column(Integer, primary_key=True, index=True, unique=True)
    book_id = Column(Integer, ForeignKey("books.book_id"))
    title = Column(String,nullable=False)
    author = Column(String, nullable=False)
    price = Column(Integer,nullable=False)
    counts = Column(Integer,nullable=False, default=1)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False)
    created_by =Column(Integer)
    updated_at = Column(DateTime)
    updated_by = Column(Integer)
    
    Cart_books = relationship("Books", back_populates="Books_cart")

