from configuration.config import *
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, ARRAY, Float
from sqlalchemy.orm import relationship

class Review(Base):
    __tablename__ = "review"

    review_id = Column(Integer, primary_key=True, unique=True)
    book_id = Column(Integer,ForeignKey("books.book_id"))
    customer_id = Column(Integer,ForeignKey("customer.customer_id"))
    review_points = Column(Float, nullable=False)
    review_comment = Column(String,nullable=False)
    is_deleted = Column(Boolean,nullable=False, default=False)
    created_at = Column(DateTime, nullable=False)
    created_by = Column(Integer,nullable= False)
    updated_at = Column(DateTime)
    updated_by = Column(Integer)

    Review_books = relationship("Books", back_populates="Books_review")
    Review_customer = relationship("Customer", back_populates="Customer_review")
