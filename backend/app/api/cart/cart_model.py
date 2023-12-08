from configuration.config import *
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, ARRAY, JSON
from sqlalchemy.orm import relationship

class Cart(Base):
    __tablename__ = "cart"

    cart_id = Column(Integer, primary_key=True, index=True, unique=True)
    book_id = Column(Integer, ForeignKey("books.book_id"))
    customer_id = Column(Integer, ForeignKey("customer.customer_id"), nullable=False)
    title = Column(String,nullable=False)
    author = Column(String, nullable=False)
    price = Column(Integer,nullable=False)
    counts = Column(Integer,nullable=False, default=1)
    total = Column(Integer,nullable=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False)
    created_by =Column(Integer)
    updated_at = Column(DateTime)
    updated_by = Column(Integer)
    
    Cart_books = relationship("Books", back_populates="Books_cart")
    Cart_customer = relationship("Customer", back_populates="Customer_cart")

class Sales(Base):
    __tablename__ = "sales"

    sales_id = Column(Integer, primary_key=True, unique=True, index=True)
    book_id = Column(ARRAY(Integer))
    customer_id = Column(Integer, ForeignKey("customer.customer_id"))
    books_quantity = Column(JSON)
    total_quantity = Column(Integer)
    price_per_book = Column(JSON)
    total_price = Column(Integer)
    created_at = Column(DateTime)

    # Sales_books = relationship("Books", back_populates="Books_sales")
    Sales_customers = relationship("Customer", back_populates="Customers_sales")

