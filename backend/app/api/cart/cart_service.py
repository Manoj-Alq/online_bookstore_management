from .cart_model import *
from utils.handlers import errorhandler
from fastapi.responses import JSONResponse
from datetime import datetime
from razorpay import Client
from api.books.books_models import Books

RAZORPAY_KEY_ID = "rzp_test_RAMJ99EXsBQTjs"
RAZORPAY_KEY_SECRET = "cHM6NdajU4bfG1RIJUJkv0CW"

client = Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

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

def createcartsService(db, cart, customer_id,db_books):
    try:
        db_cart = Cart(
            book_id = db_books.book_id,
            customer_id = customer_id,
            title = db_books.title,
            author = db_books.author,
            price = db_books.price,
            counts = cart.counts,
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            created_by = customer_id,
            total = db_books.price * cart.counts
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
                db_cart.total = cart.counts * db_cart.price
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

def buyBookService(db,amount, carts_db):
    order_data = {
        "amount": amount * 100,
        "currency": "INR",
        "payment_capture": 1
    }

    try:
        response = client.order.create(data=order_data)
        order_id = response['id']
        # payment_id = response['payment'][0]['id']
        for i in carts_db:
            i.is_deleted = True
            db.commit()
             
        return response
    except Exception as e:
        errorhandler(400,f"order errors{e}")

    # Use test card details for payment

def verify_payment(db,order_id, payment_id, books_quantity, book_ids, customer_id, total_quantity, price_per_book, total_price):
    try:
        # Verify the payment with Razorpay
        payment = client.payment.fetch(payment_id)
        # Check the payment status
        if payment['status'] == 'captured':
            db_sales = Sales(
                book_id = book_ids,
                customer_id = customer_id,
                books_quantity = books_quantity,
                total_quantity = total_quantity,
                price_per_book = price_per_book,
                total_price = total_price,
                created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            )
            db.add(db_sales)
            db.commit()
            return {"status": "Payment successful"}
        else:
            return {"status": "Payment failed"}
    except Exception as e:
        errorhandler(400,f"{e}")
