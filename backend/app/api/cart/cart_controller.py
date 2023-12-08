from .cart_service import *
from utils.validations import Validations
from utils.auth_handlers import *

validation = Validations()

def getAllcartController(db):
    return getAllcartservice(db)

def getSinglecartController(db, id):
    db_cart = db.query(Cart).filter(Cart.cart_id == id, Cart.is_deleted == False).first()
    if db_cart is None:
        errorhandler(404,"cart not found")
    return getSingleCartService(db,db_cart)

def createcartController(db,cart, Auth_head,book_id):
    db_book = db.query(Books).filter(Books.book_id == book_id).first()
    if db_book == None:
        errorhandler(404,"Book not found")
    customer_id  = decode_token_id(Auth_head)
    if validation.None_validation(cart.counts):
        errorhandler(400, "count field is required")
    if validation.empty_validation(cart):
        key = validation.empty_key_validation(cart)
        errorhandler(400, f"{key} shouldn't be empty")
    return createcartsService(db, cart,customer_id,db_book)

def updatecartController(db,cart, id):
    db_book = db.query(Cart).filter(Cart.cart_id == id, Cart.is_deleted == False).first()
    if db_book == None:
        errorhandler(404, "book not found")
    return updatecartservice(db,db_book,cart)

def deletecartController(db, Auth_head, id):
    db_cart = db.query(Cart).filter(Cart.cart_id == id, Cart.is_deleted == False).first()
    if db_cart == None:
        errorhandler(404, "cart not found")
    
    return deletecartervice(db,db_cart)

def buyBooksController(db,Auth_head,request):
    customer_id  = decode_token_id(Auth_head)
    carts_db = db.query(Cart).filter(Cart.created_by == customer_id,Cart.is_deleted == False).all()
    total_amount = 0
    for i in carts_db:
        total_amount += i.total

    if total_amount <= 0:
        errorhandler(400,"Amout should be greater than 0")

    return buyBookService( db,total_amount, carts_db)

def verify_payment_controller(db,order_id,payment_id,cart_ids):
    db_carts = db.query(Cart).filter(Cart.cart_id.in_(cart_ids)).all()
    if db_carts == None:
        errorhandler(404, "carts are not found")
    book_ids = []
    books_quantity = {}
    total_quatity = 0
    customer_id = int
    price_per_book = {}
    total_price = 0
    for i in db_carts:
        book_ids.append(i.book_id)
        books_quantity[f"{i.book_id}"] = f"{i.counts}"
        price_per_book[f"{i.book_id}"] = f"{i.price}"
        customer_id = i.customer_id
        total_quatity += i.counts
        total_price += i.total
    return verify_payment(db,order_id, payment_id, books_quantity, book_ids, customer_id, total_quatity, price_per_book, total_price)