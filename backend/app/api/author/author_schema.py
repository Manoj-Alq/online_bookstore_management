from pydantic import BaseModel
from datetime import date, datetime

class AuthorResponse(BaseModel):
    Author_id : int = None
    firts_name : str = None
    last_name : str = None
    email : str = None
    DOB : date = None
    bio : str = None
    twitter_handle : str = None
    nationality : str = None
    websitelink : str = None
    fav_genres : list = None
    phone_number : str = None
    username : str = None
    created_at : datetime = None

class AuthorSignUp(BaseModel):
    first_name : str = None
    last_name : str = None
    email : str = None
    DOB : date = None
    bio : str = None
    twitter_handle : str = None
    nationality : str = None
    websitelink : str = None
    fav_genres : list = None
    phone_number : str = None
    username : str = None
    password : str = None

class AuthorLogIn(BaseModel):
    username : str = None
    password : str = None
