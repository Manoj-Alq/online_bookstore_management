from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class cartresponse(BaseModel):
    cart_id : int = None
    title : str =  None
    author : str = None
    price : int = None
    counts : int = None
    total : int = None
    created_at : datetime = None
    created_by : Optional[int]
    updated_at : Optional[datetime]
    updated_by : Optional[int] 

class create_cart(BaseModel):
    title : str =  None
    author : str = None
    price : int = None
    counts : int = None