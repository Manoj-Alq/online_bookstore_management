from .customer_service import *
from utils.auth_handlers import *
from utils.validations import *
from api.admin.admin_model import AdminToken

validation = Validations()

def getAllcustomerController(db):
    return getAllcustomerService(db)

def getSinglecustomerController(db,id):
    db_customer = db.query(Customer).filter(Customer.customer_id == id, Customer.is_deleted == False).first()
    if db_customer is None:
        errorhandler(404,"customer not found")
    return getSinglecustomerService(db,db_customer)

def signupcustomerController(db, customer):
    # admin_id = decode_token_id(Auth_head, model=customerToken, db=db)
    if validation.None_validation(
        customer.first_name,customer.last_name,customer.email,customer.DOB,customer.bio,customer.twitter_handle,customer.nationality,customer.websitelink,customer.fav_genres,customer.phone_number,customer.username,customer.password
    ):
        print(customer.first_name,customer.last_name,customer.email,customer.DOB,customer.bio,customer.twitter_handle,customer.nationality,customer.websitelink,customer.fav_genres,customer.phone_number,customer.username,customer.password)
        errorhandler(400, "All fields are required")
    if validation.empty_validation(customer):
        key = validation.empty_key_validation(customer)
        errorhandler(400, f"{key} shouldn't be empty")
    if validation.duplication_username_validate(db,Customer,customer.username):
         errorhandler(400,"username is not avaiable")
    if len(customer.username ) < 5:
         errorhandler(400, "username should have more than 5 characters")
    if not validation.email_validations(customer.email):
        errorhandler(400, "Invalid email")
    if validation.duplication_email_validate(db,Customer,customer.email):
         errorhandler(400,"email is not avaiable")
    if not validation.phoneNumber_validation(customer.phone_number):
        errorhandler(400,"Invalid phone number ")
    if not validation.password_validation(customer.password):
        errorhandler(400, "Password should contain 8 character, atleast 1 uppercase letter, atleast 1 lowercase letter, atleast 1 symbol")
    return signupcustomerService(db, customer)

def logIncustomerController(db,customer):
    if validation.None_validation(customer.username,customer.password
    ):
        errorhandler(400, "All fields are required")
    if validation.empty_validation(customer):
        key = validation.empty_key_validation(customer)
        errorhandler(400, f"{key} shouldn't be empty")
    db_customer = authenticate_user(db,customer.username, customer.password,Customer)
    if db_customer != None:
        if validation.User_delete_validation(db_customer):
            errorhandler(400, "customer not found")
        if validation.login_validation(db_customer):
            errorhandler(400, "You're already loggedin")
    
    return logincustomerService(db, customer, db_customer)

def getMyProfileController(db,Auth_head):
    customer_id = decode_token_id(Auth_head,model=CustomerToken,db=db)
    print('id',customer_id)
    db_customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if validation.User_delete_validation(db_customer):
        errorhandler(404,"User not found")   

    return getMyProfileService(db, db_customer)

def updatecustomerController(db,customer,Auth_head,id,role):
    if role == "admin":
        if id != None:
            admin_id = decode_token_id(Auth_head, model=AdminToken, db=db)
            db_customer = db.query(Customer).filter(Customer.customer_id == id).first()
        else:
            errorhandler(403, "Id must for admin")
    else:
        customer_id = decode_token_id(Auth_head, model=CustomerToken, db=db)
        db_customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
        print(db_customer.username)
    if db_customer == None:
         errorhandler(404, "customer not found")
    if db_customer != None:
        if validation.User_delete_validation(db_customer):
            errorhandler(400, "customer not found")
    if validation.duplication_username_validate(db,Customer,customer.username):
         errorhandler(400,"username is not avaiable")
    if customer.email:
        if not validation.email_validations(customer.email):
            errorhandler(400, "Invalid email")
    if customer.phone_number:
        if not validation.phoneNumber_validation(customer.phone_number):
            errorhandler(400,"Invalid phone number")
    if customer.password:
        if not validation.password_validation(customer.password):
            errorhandler(400, "Password should contain 8 character, atleast 1 uppercase letter, atleast 1 lowercase letter, atleast 1 symbol")
    return updatecustomerService(db,customer,db_customer)

def logoutcustomerController(db,Auth_head,id,role):
    if role == "admin":
            if id != None:
                admin_id = decode_token_id(Auth_head, model=AdminToken, db=db)
                db_customer = db.query(Customer).filter(Customer.customer_id == id).first()
                if db_customer.is_active == False:
                        errorhandler(400, f"{id} is not loggedin yet")
            else:
                errorhandler(400,"Id must for Admin")
            
    else:
        if id != None:
            errorhandler(403,"You cant't logout others account")
        customer_id = decode_token_id(Auth_head, model=CustomerToken, db=db)
        db_customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
        print("customer",customer_id)

    if validation.User_delete_validation(db_customer):
            errorhandler(404,"customer not found")   


    return signoutcustomerService(db, db_customer)

def deletecustomerController(db,Auth_head,id,role):
    if id != None:
        if role == "admin":
            admin_id = decode_token_id(Auth_head, model=AdminToken, db=db)
            db_customer = db.query(Customer).filter(Customer.customer_id == id).first()
        else:
            errorhandler(400,"You can't delete another acoount")
    else:
        if role == "admin":
            errorhandler(400,"Id must for admin")
        customer_id = decode_token_id(Auth_head, model=CustomerToken, db=db)
        db_customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if db_customer == None:
        errorhandler(404,"customer not found")
        print(db_customer, "customer")
    if validation.User_delete_validation(db_customer):
        errorhandler(404,"customer not found")   
    return deletecustomerService(db, db_customer)