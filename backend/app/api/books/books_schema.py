from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class Booksresponse(BaseModel):
    title : str =  None
    author : str = None
    publisher : str = None
    publication_year : int = None
    isbn : int = None
    genre : list = None
    description : str = None
    language : str = None
    number_of_pages : int = None
    cover_image : str = None
    average_rating : int = None
    price : int = None
    availability : bool = None
    date_added : datetime = None
    last_updated : Optional[datetime]

class Create_book(BaseModel):
    title : str =  None
    author : str = None
    publisher : str = None
    publication_year : int = None
    isbn : int = None
    genre : list = None
    description : str = None
    language : str = None
    number_of_pages : str = None
    cover_image : str = None
    average_rating : float = None
    price : int = None