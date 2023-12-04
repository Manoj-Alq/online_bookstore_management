from utils.handlers import errorhandler
from .customer_model import *
from utils.auth_handlers import *
from fastapi.responses import JSONResponse

expiry_del = ACCESS_TOKEN_EXPIRY_MINUTES

def getAllcustomerService(db):
    try: 
        db_customers = db.query(Customer).filter(Customer.is_deleted == False).all()
        return db_customers
    except Exception as e:
        db.rollback()
        errorhandler(400,f"{e}")

def getSinglecustomerService(db,db_customer):
    try:
        return db_customer
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def signupcustomerService(db, customer):
    try:
        db_customer = Customer(
            first_name=customer.first_name,
            last_name = customer.last_name,
            email=customer.email,
            DOB = customer.DOB,
            bio = customer.bio,
            twitter_handle = customer.twitter_handle,
            nationality = customer.nationality,
            websitelink = customer.websitelink,
            fav_genres = customer.fav_genres,
            phone_number=customer.phone_number,
            username=customer.username,
            password=hash_password(customer.password),
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            # created_by=customer_id
        )

        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)

        return JSONResponse({
            "message": "customer created successfully"
        })
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def logincustomerService(db, customer, db_customer):
    try:
        db_customer.is_active = True
        access_token = create_access_token(data={"sub": str(db_customer.customer_id),"role": str("customer")}, expires_delta=expiry_del)
        db_token = CustomerToken(customer_id=db_customer.customer_id, token=access_token)
        db.add(db_token)
        db.commit()           
        return JSONResponse(status_code=200, content={
            "message": "User loggedin successfully",
            "status": "ok",
            "username": db_customer.username,
            "access_token": access_token,
            "token_type": "bearer",
            "email": db_customer.email,
            "first-name": db_customer.first_name,
            "phone_number": db_customer.phone_number,
            "customer_id": db_customer.customer_id,
            "username": db_customer.username
        })
    except Exception as e:
        print(e)

def getMyProfileService(db, db_customer):
    try:
        print("service customer",db_customer.created_at)
        return db_customer
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def updatecustomerService(db,customer,db_customer):
    try:
        # db_customer = db.query(customer).filter(customer.customer_id == id).first()
        if customer.username != "" and customer.username != None:
            db_customer.username = customer.username
        if customer.first_name != "" and customer.first_name != None:
            db_customer.first_name = customer.first_name
        if customer.last_name != "" and customer.last_name != None:
            db_customer.last_name = customer.last_name
        if customer.password != "" and customer.password != None:
            db_customer.password = hash_password(customer.password)
        if customer.email != "" and customer.email != None:
            db_customer.email = customer.email
        if customer.phone_number != "" and customer.phone_number != None:
            db_customer.phone_number = customer.phone_number
        db_customer.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.commit()

        return JSONResponse({
            "message": "customer updated successfully"
        })

    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def signoutcustomerService(db, db_customer):
    try:
        db_customer.is_active = False
        db_token = db.query(CustomerToken).filter(
            CustomerToken.customer_id == db_customer.customer_id).first()
        if db_token != None:
            db.delete(db_token)
        db.commit()
        return JSONResponse({
            "message": "logged out successfully"
        })
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def deletecustomerService(db, db_customer):
    try:
        db_customer.is_deleted = True
        db_token = db.query(CustomerToken).filter(
            CustomerToken.customer_id == db_customer.customer_id).first()
        if db_token != None:
            db.delete(db_token)
        db.commit()
        return JSONResponse({
            "message": "customer deleted successfully"
        })
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")