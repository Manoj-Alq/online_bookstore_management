from .books_models import *
from utils.handlers import errorhandler
from datetime import datetime
from fastapi.responses import JSONResponse
import base64
from io import BytesIO
from PIL import Image

def getAllbooksservice(db):
    try:
        db_books= db.query(Books).filter(Books.is_deleted == False).all()
        # time.sleep(2)
        return db_books
    except Exception as e:
        db.rollback()
        errorhandler(400,f"{e}")

def getSingleBooksService(db,db_books):
    try:
        return db_books
    except Exception as e:
        db.rollback()
        errorhandler(400,f"{e}")

def createBooksService(db, book):
    try:
        print("book title",book.title)
        cover = BytesIO(base64.b64decode(book.cover_image))
        coverImage = Image.open(cover)
        filename = f"image_{book.title}.png"
        local_path = f"D:/practice/projects/online_bookstore_management/backend/images/books/{filename}"
        coverImage.save(local_path)

        print(cover)

        db_book = Books(
            title = book.title,
            author = book.author,
            publisher = book.publisher,
            publication_year = book.publication_year,
            isbn = book.isbn,
            genre = book.genre,
            description = book.description,
            language = book.language,
            number_of_pages = book.number_of_pages,
            cover_image = local_path,
            average_rating = book.average_rating,
            price = book.price,
            availability = False,
            date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        )
        db.add(db_book)
        db.commit()
        db.refresh(db_book)

        return JSONResponse({
            "message":"Book created successfully"
        })
    
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def updatebookservice(db,db_book,book):
    try:
        if book.title != "" and book.title != None:
                db_book.title = book.title
        if book.author != "" and book.author != None:
                db_book.author = book.author
        if book.publisher != "" and book.publisher != None:
                db_book.publisher = book.publisher
        if book.publication_year != "" and book.publication_year != None:
                db_book.publication_year = book.publication_year
        if book.isbn != "" and book.isbn != None:
                db_book.isbn = book.isbn
        if book.genre != "" and book.genre != None:
                db_book.genre = book.genre
        if book.description != "" and book.description != None:
                db_book.description = book.description
        if book.language != "" and book.language != None:
                db_book.language = book.language
        if book.number_of_pages != "" and book.number_of_pages != None:
                db_book.number_of_pages = book.number_of_pages
        if book.cover_image != "" and book.cover_image != None:
                cover = BytesIO(base64.b64decode(book.cover_image))
                coverImage = Image.open(cover)
                filename = f"image_{db_book.title}updated.png"
                local_path = f"D:/practice/projects/online_bookstore_management/backend/images/books/{filename}"
                coverImage.save(local_path)
                db_book.cover_image = local_path
        if book.average_rating != "" and book.average_rating != None:
                db_book.average_rating = book.average_rating
        if book.price != "" and book.price != None:
                db_book.price = book.price
        db_book.last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.commit()

        return JSONResponse({
            "message":"book updated successfully"
        })
    
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def deletebookService(db,db_books):
    try:
        db_books.is_deleted = True
        db.commit()
        return JSONResponse({
            "message":"book deleted successfully"
        })
    except Exception as e:
        db.rollback()
        errorhandler(400,f"{e}")