from .admin_model import *
from datetime import datetime
from fastapi.responses import JSONResponse
from utils.auth_handlers import *
from utils.handlers import *

expiry_del = ACCESS_TOKEN_EXPIRY_MINUTES

def getAlladminService(db):
    try:
        db_admins = db.query(Admin).filter(Admin.is_deleted == False).all()
        return db_admins
    except Exception as e:
        db.rollback()
        errorhandler(400,f"{e}")

def getSingleadminService(db, db_admin):
    try:
        return db_admin
    except Exception as e:
        db.rollback()
        errorhandler(400,f"{e}")

def signupService(db, admin):
    try:
        db_admin = Admin(
            name = admin.name,
            email = admin.email,
            phone_number = admin.phone_number,
            username = admin.username,
            password = hash_password(admin.password),
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        
        db.add(db_admin)
        db.commit()
        db.refresh(db_admin)

        return JSONResponse({
            "message":"User created successfully"
        })
    
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def signinService(db, admin, db_admin):
        db_admin.is_active = True
        signin_log = AdminSigninLogs(admin_id= db_admin.admin_id, loggedin = datetime.now())
        access_token = create_access_token(data={"sub": str(db_admin.admin_id),"role": str("admin")}, expires_delta=expiry_del)
        db_token = AdminToken(admin_id= db_admin.admin_id, token=access_token)
        db.add(signin_log)
        db.add(db_token)
        db.commit()           
        return JSONResponse({
            "message":"User loggedin successfully",
            "user":{
                "username":admin.username,
                "access_token": access_token, 
                "token_type": "bearer"}
            })

def getMyProfileService(db, db_user):
          try:
            return db_user
          except Exception as e:
            db.rollback()
            errorhandler(400,f"{e}")

def updateadminService(db,admin,db_admin):
    try:
        if admin.username != "" and admin.username != None:
                print("username")
                db_admin.username = admin.username
        if admin.name != "" and admin.name != None:   
                    db_admin.name = admin.name
        if admin.password != "" and admin.password != None:
                    print(admin.password)   
                    db_admin.password = hash_password(admin.password)
        if admin.email != "" and admin.email != None:   
                    db_admin.email = admin.email
        if admin.phone_number != "" and admin.phone_number != None:   
                    db_admin.phone_number = admin.phone_number
        db_admin.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.commit()


        return JSONResponse({
            "message":"admin updated successfully"
        })
    
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def signOutService(db, db_admin,db_token):
          try:
            db_admin.is_active = False
            signin_user = db.query(AdminSigninLogs).filter(AdminSigninLogs.admin_id == db_admin.admin_id).all()
            list_signin = [i.id for i in signin_user]
            last_login_id = max(list_signin)
            last_login = db.query(AdminSigninLogs).filter(AdminSigninLogs.id == last_login_id).first()
            last_login.loggedout = datetime.now() 
            db.delete(db_token)
            db.commit()
            return JSONResponse({
                  "message":"logged out successfully"
            })
          except Exception as e:
            db.rollback()
            errorhandler(400,f"{e}")

def deleteadminService(db, db_admin):
          try:
            print(db_admin.is_deleted)
            db_admin.is_deleted = True
            db_token = db.query(AdminToken).filter(AdminToken.admin_id == db_admin.admin_id).first()
            if db_token != None:
                db.delete(db_token)
            db.commit()
            return JSONResponse({
                  "message":"admin deleted successfully"
            })
          except Exception as e:
            db.rollback()
            errorhandler(400,f"{e}")