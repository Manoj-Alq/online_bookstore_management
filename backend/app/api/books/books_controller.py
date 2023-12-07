from .books_service import *
from utils.validations import Validations

validation = Validations()

def getAllbooksController(db,search,page,page_size,publication_year,genre):
    return getAllbooksservice(db,search,page,page_size,publication_year,genre)

def getSingleBooksController(db, id):
    db_books = db.query(Books).filter(Books.book_id == id, Books.is_deleted == False).first()
    if db_books is None:
        errorhandler(404,"book not found")
    return getSingleBooksService(db,db_books)

def createBookController(db,book):
    if validation.None_validation(book.title, book.author, book.publisher, book.publication_year, book.isbn, book.genre,book.description, book.language, book.number_of_pages,book.cover_image,book.average_rating,book.price):
        errorhandler(400, "All field's are required")
    print("book",type(book))
    if validation.empty_validation(book):
        key = validation.empty_key_validation(book)
        errorhandler(400, f"{key} shouldn't be empty")
    return createBooksService(db, book)

def updatebookController(db,book, id):
    db_book = db.query(Books).filter(Books.book_id == id, Books.is_deleted == False).first()
    if db_book == None:
        errorhandler(404, "book not found")
    return updatebookservice(db,db_book,book)

def deletebookController(db, Auth_head, id):
    db_books = db.query(Books).filter(Books.book_id == id, Books.is_deleted == False).first()
    if db_books == None:
        errorhandler(404, "books not found")
    
    return deletebookService(db,db_books)
