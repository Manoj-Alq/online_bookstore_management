from .cart_model import Cart
from utils.handlers import errorhandler
from fastapi.responses import JSONResponse
from datetime import datetime
from razorpay import Client
import json

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

def createcartsService(db, cart, customer_id):
    try:
        db_cart = Cart(
            title = cart.title,
            author = cart.author,
            price = cart.price,
            counts = cart.counts,
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            created_by = customer_id,
            total = cart.price * cart.counts
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

def buyBookService(amount):
    order_data = {
        "amount": amount,
        "currency": "INR",
        "payment_capture": 1
    }

    try:
        response = client.order.create(data=order_data)
        order_id = response['id']
        # payment_id = response['payment'][0]['id']
        return response
    except Exception as e:
        errorhandler(400,f"order errors{e}")

    # Use test card details for payment

def verify_payment(order_id: str, payment_id: str):
    try:
        # Verify the payment with Razorpay
        payment = client.payment.fetch(payment_id)

        # Check the payment status
        if payment['status'] == 'captured':
            return {"status": "Payment successful"}
        else:
            return {"status": "Payment failed"}
    except Exception as e:
        errorhandler(400,f"{e}")
