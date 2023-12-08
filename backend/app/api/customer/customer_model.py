from configuration.config import *
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, ARRAY
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column(Integer, primary_key=True,index=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    DOB = Column(DateTime)
    bio = Column(String)
    twitter_handle = Column(String)
    nationality = Column(String)
    websitelink = Column(String)
    fav_genres = Column(ARRAY(String))
    phone_number = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
    is_active = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime)
    created_by = Column(Integer)
    updated_at = Column(DateTime)
    updated_by = Column(Integer)

    Customer_signinlogs = relationship("CustomerSigninLogs", back_populates="signinlogs_Customer")
    Customertoken = relationship("CustomerToken", back_populates="tokenCustomer")
    Customer_review = relationship("Review", back_populates="Review_customer")
    Customer_cart = relationship("Cart", back_populates="Cart_customer")
    Customers_sales = relationship("Sales", back_populates="Sales_customers")
    
class CustomerSigninLogs(Base):
    __tablename__ = "customer_signin_logs"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    customer_id = Column(Integer, ForeignKey("customer.customer_id"))
    loggedin = Column(DateTime)
    loggedout = Column(DateTime)

    signinlogs_Customer = relationship("Customer", back_populates="Customer_signinlogs")

class CustomerToken(Base):
    __tablename__ = "customer_tokens"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    customer_id = Column(Integer, ForeignKey("customer.customer_id"))
    token = Column(String,unique=True)

    tokenCustomer = relationship("Customer", back_populates="Customertoken")