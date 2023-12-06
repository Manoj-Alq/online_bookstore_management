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

def createcartController(db,cart, Auth_head):
    customer_id  = decode_token_id(Auth_head)
    if validation.None_validation(cart.title, cart.author,cart.price):
        errorhandler(400, "All field's are required")
    if validation.empty_validation(cart):
        key = validation.empty_key_validation(cart)
        errorhandler(400, f"{key} shouldn't be empty")
    return createcartsService(db, cart,customer_id)

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

def buyBooksController(db,Auth_head):
    customer_id  = decode_token_id(Auth_head)
    carts_db = db.query(Cart).filter(Cart.created_by == customer_id,Cart.is_deleted == False).all()
    total_amount = 0
    for i in carts_db:
        total_amount += i.total

    if total_amount <= 0:
        errorhandler(400,"Amout should be greater than 0")

    return buyBookService( total_amount)