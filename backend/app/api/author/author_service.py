from utils.handlers import errorhandler
from .author_model import *
from utils.auth_handlers import *
from fastapi.responses import JSONResponse

expiry_del = ACCESS_TOKEN_EXPIRY_MINUTES

def getAllAuthorService(db):
    try: 
        db_authors = db.query(Author).filter(Author.is_deleted == False).all()
        return db_authors
    except Exception as e:
        db.rollback()
        errorhandler(400,f"{e}")

def getSingleAuthorService(db,db_Author):
    try:
        return db_Author
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def signupAuthorService(db, author):
    try:
        db_author = Author(
            firts_name=author.first_name,
            last_name = author.last_name,
            email=author.email,
            DOB = author.DOB,
            bio = author.bio,
            twitter_handle = author.twitter_handle,
            nationality = author.nationality,
            websitelink = author.websitelink,
            fav_genres = author.fav_genres,
            phone_number=author.phone_number,
            username=author.username,
            password=hash_password(author.password),
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            # created_by=author_id
        )

        db.add(db_author)
        db.commit()
        db.refresh(db_author)

        return JSONResponse({
            "message": "author created successfully"
        })
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def loginAuthorService(db, author, db_author):
    try:
        db_author.is_active = True
        access_token = create_access_token(data={"sub": str(db_author.Author_id),"role": str("author")}, expires_delta=expiry_del)
        db_token = AuthorToken(Author_id=db_author.Author_id, token=access_token)
        db.add(db_token)
        db.commit()           
        return JSONResponse(status_code=200, content={
            "message": "User loggedin successfully",
            "status": "ok",
            "username": db_author.username,
            "access_token": access_token,
            "token_type": "bearer",
            "email": db_author.email,
            "first-name": db_author.firts_name,
            "phone_number": db_author.phone_number,
            "author_id": db_author.Author_id,
            "username": db_author.username
        })
    except Exception as e:
        print(e)

def getMyProfileService(db, db_author):
    try:
        print("service author",db_author.created_at)
        return db_author
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def updateAuthorService(db,author,db_author):
    try:
        # db_author = db.query(Author).filter(Author.Author_id == id).first()
        if author.username != "" and author.username != None:
            db_author.username = author.username
        if author.first_name != "" and author.first_name != None:
            db_author.firts_name = author.first_name
        if author.last_name != "" and author.last_name != None:
            db_author.last_name = author.last_name
        if author.password != "" and author.password != None:
            db_author.password = hash_password(author.password)
        if author.email != "" and author.email != None:
            db_author.email = author.email
        if author.phone_number != "" and author.phone_number != None:
            db_author.phone_number = author.phone_number
        db_author.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.commit()

        return JSONResponse({
            "message": "author updated successfully"
        })

    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def signoutAuthorService(db, db_author):
    try:
        db_author.is_active = False
        db_token = db.query(AuthorToken).filter(
            AuthorToken.Author_id == db_author.Author_id).first()
        if db_token != None:
            db.delete(db_token)
        db.commit()
        return JSONResponse({
            "message": "logged out successfully"
        })
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def deleteAuthorService(db, db_author):
    try:
        db_author.is_deleted = True
        db_token = db.query(AuthorToken).filter(
            AuthorToken.Author_id == db_author.Author_id).first()
        if db_token != None:
            db.delete(db_token)
        db.commit()
        return JSONResponse({
            "message": "author deleted successfully"
        })
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")