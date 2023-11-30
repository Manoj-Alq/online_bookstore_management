from configuration.config import *
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Admin(Base):
    __tablename__ = "admin"

    admin_id = Column(Integer, primary_key=True,index=True, unique=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
    is_active = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    admin_signinlogs = relationship("AdminSigninLogs", back_populates="signinlogs_admin")
    admintoken = relationship("AdminToken", back_populates="tokenadmin")
    
class AdminSigninLogs(Base):
    __tablename__ = "admin_signin_logs"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    admin_id = Column(Integer, ForeignKey("admin.admin_id"))
    loggedin = Column(DateTime)
    loggedout = Column(DateTime)

    signinlogs_admin = relationship("Admin", back_populates="admin_signinlogs")

class AdminToken(Base):
    __tablename__ = "admin_tokens"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    admin_id = Column(Integer, ForeignKey("admin.admin_id"))
    token = Column(String,unique=True)

    tokenadmin = relationship("Admin", back_populates="admintoken")