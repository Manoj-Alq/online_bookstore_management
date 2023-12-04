from pydantic import BaseModel
from datetime import date, datetime

class CustomerResponse(BaseModel):
    customer_id : int = None
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
    created_at : datetime = None

class CustomerSignUp(BaseModel):
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

class CustomerLogIn(BaseModel):
    username : str = None
    password : str = None
