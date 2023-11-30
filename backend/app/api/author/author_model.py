from configuration.config import *
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, ARRAY
from sqlalchemy.orm import relationship

class Author(Base):
    __tablename__ = "Author"

    Author_id = Column(Integer, primary_key=True,index=True, unique=True)
    firts_name = Column(String)
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

    Author_signinlogs = relationship("AuthorSigninLogs", back_populates="signinlogs_Author")
    Authortoken = relationship("AuthorToken", back_populates="tokenAuthor")
    
class AuthorSigninLogs(Base):
    __tablename__ = "Author_signin_logs"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    Author_id = Column(Integer, ForeignKey("Author.Author_id"))
    loggedin = Column(DateTime)
    loggedout = Column(DateTime)

    signinlogs_Author = relationship("Author", back_populates="Author_signinlogs")

class AuthorToken(Base):
    __tablename__ = "Author_tokens"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    Author_id = Column(Integer, ForeignKey("Author.Author_id"))
    token = Column(String,unique=True)

    tokenAuthor = relationship("Author", back_populates="Authortoken")