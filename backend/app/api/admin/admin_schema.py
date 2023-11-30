from pydantic import BaseModel, Field
from datetime import datetime

class AdminResponse(BaseModel):
    admin_id : int = None
    name : str = None
    email : str = None
    phone_number : str = None
    username : str = None
    created_at : datetime = None

class AdminSignUp(BaseModel):
    name : str = Field(None, title="")
    email : str = None
    phone_number : str = None
    username : str = None
    password : str = None

class AdminSignIn(BaseModel):
    username : str = None
    password : str = None
