from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List
from utils.auth import *
from configuration.config import *
from .books_schema import *
from .books_controller import *

httpbearer = AdminJWT()

@router.get("/books/getAllbooks",response_model=List[Booksresponse], tags=["books"])
async def getAllbook(db: Session = Depends(get_session)):
    return getAllbooksController(db)
    # return

@router.get("/books/getabooks/{id}",response_model=Booksresponse, tags=["books"])
async def getSinglebook(id:int,db: Session = Depends(get_session)):
    return getSingleBooksController(db, id)
    # return 

@router.post("/books/createbooks", response_model=Booksresponse, tags=["books"], summary="author can signup here")
async def createbook(book: Create_book,role:str = Depends(author_authorization),db: Session = Depends(get_session)):
    return createBookController(db, book)
    # return

@router.post("/books/updatebooks",dependencies = [Depends(httpbearer)],response_model=Booksresponse, tags=["books"])
async def updatebook(book: Create_book,id:int,role:str = Depends(author_authorization),Auth_head:str = Depends(get_authorization_header),db: Session = Depends(get_session)):
    return updatebookController(db,book, id)
    # return

@router.post("/books/deletebooks",dependencies = [Depends(httpbearer)],response_model=Booksresponse, tags=["books"])
async def signupbook(id:int = None,role:str = Depends(author_authorization),Auth_head:str = Depends(get_authorization_header),db: Session = Depends(get_session)):
    return deletebookController(db, Auth_head, id)
    # return