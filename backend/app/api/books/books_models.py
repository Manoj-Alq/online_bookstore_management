from configuration.config import *
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, ARRAY
from sqlalchemy.orm import relationship

class Books(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publisher = Column(String, nullable=False)
    publication_year = Column(Integer, nullable=False)
    isbn = Column(String, nullable=False)
    genre = Column(ARRAY(String),nullable=False)
    description = Column(String,nullable=False)
    language = Column(String, nullable=False)
    number_of_pages =Column(Integer, nullable=False)
    cover_image = Column(String,nullable=False)
    average_rating = Column(Integer)
    price = Column(Integer,nullable=False)
    sales_count = Column(Integer,nullable=False,default=0)
    availability = Column(Boolean,nullable=False)
    is_deleted = Column(Boolean, default=False)
    date_added = Column(DateTime, nullable=False)
    last_updated = Column(DateTime)

    Books_cart = relationship("Cart",back_populates="Cart_books")
    Books_review = relationship("Review",back_populates="Review_books")
    # Books_sales = relationship("Sales", back_populates="Sales_books")
