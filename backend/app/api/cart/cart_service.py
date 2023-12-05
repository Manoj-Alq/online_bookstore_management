from .cart_model import Cart
from utils.handlers import errorhandler
from fastapi.responses import JSONResponse
from datetime import datetime

def getAllcartservice(db):
    try:
        db_cart= db.query(Cart).filter(Cart.is_deleted == False).all()
        # time.sleep(2)
        return db_cart
    except Exception as e:
        db.rollback()
        errorhandler(400,f"{e}")

def getSingleCartService(db,db_cart):
    try:
        return db_cart
    except Exception as e:
        db.rollback()
        errorhandler(400,f"{e}")

def createcartsService(db, cart):
    try:
        db_cart = Cart(
            title = cart.title,
            author = cart.author,
            price = cart.price,
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        db.add(db_cart)
        db.commit()
        db.refresh(db_cart)

        return JSONResponse({
            "message":"cart created successfully"
        })
    
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def updatecartservice(db,db_cart,cart):
    try:
        if cart.title != "" and cart.title != None:
                db_cart.title = cart.title
        if cart.author != "" and cart.author != None:
                db_cart.author = cart.author
        if cart.price != "" and cart.price != None:
                db_cart.price = cart.price
        if cart.counts != "" and cart.counts != None:
                db_cart.counts = cart.counts
        db_cart.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.commit()

        return JSONResponse({
            "message":"cart updated successfully"
        })
    
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def deletecartervice(db,db_cart):
    try:
        db_cart.is_deleted = True
        db.commit()
        return JSONResponse({
            "message":"cart deleted successfully"
        })
    except Exception as e:
        db.rollback()
        errorhandler(400,f"{e}")