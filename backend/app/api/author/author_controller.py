from .author_service import *
from utils.auth_handlers import *
from utils.validations import *
from api.admin.admin_model import AdminToken

validation = Validations()

def getAllAuthorController(db):
    return getAllAuthorService(db)

def getSingleauthorController(db,id):
    db_Author = db.query(Author).filter(Author.Author_id == id, Author.is_deleted == False).first()
    if db_Author is None:
        errorhandler(404,"Author not found")
    return getSingleAuthorService(db,db_Author)

def signupAuthorController(db, author):
    # admin_id = decode_token_id(Auth_head, model=AuthorToken, db=db)
    if validation.None_validation(
        author.first_name,author.last_name,author.email,author.DOB,author.bio,author.twitter_handle,author.nationality,author.websitelink,author.fav_genres,author.phone_number,author.username,author.password
    ):
        print(author.first_name,author.last_name,author.email,author.DOB,author.bio,author.twitter_handle,author.nationality,author.websitelink,author.fav_genres,author.phone_number,author.username,author.password)
        errorhandler(400, "All fields are required")
    if validation.empty_validation(author):
        key = validation.empty_key_validation(author)
        errorhandler(400, f"{key} shouldn't be empty")
    if validation.duplication_username_validate(db,Author,author.username):
         errorhandler(400,"username is not avaiable")
    if len(author.username ) < 5:
         errorhandler(400, "username should have more than 5 characters")
    if not validation.email_validations(author.email):
        errorhandler(400, "Invalid email")
    if validation.duplication_email_validate(db,Author,author.email):
         errorhandler(400,"email is not avaiable")
    if not validation.phoneNumber_validation(author.phone_number):
        errorhandler(400,"Invalid phone number")
    if not validation.password_validation(author.password):
        errorhandler(400, "Password should contain 8 character, atleast 1 uppercase letter, atleast 1 lowercase letter, atleast 1 symbol")
    return signupAuthorService(db, author)

def logInAuthorController(db,author):
    if validation.None_validation(author.username,author.password
    ):
        errorhandler(400, "All fields are required")
    if validation.empty_validation(author):
        key = validation.empty_key_validation(author)
        errorhandler(400, f"{key} shouldn't be empty")
    db_author = authenticate_user(db,author.username, author.password,Author)
    if db_author != None:
        if validation.User_delete_validation(db_author):
            errorhandler(400, "author not found")
        if validation.login_validation(db_author):
            errorhandler(400, "You're already loggedin")
    
    return loginAuthorService(db, author, db_author)

def getMyProfileController(db,Auth_head):
    author_id = decode_token_id(Auth_head,model=AuthorToken,db=db)
    print('id',author_id)
    db_author = db.query(Author).filter(Author.Author_id == author_id).first()
    if validation.User_delete_validation(db_author):
        errorhandler(404,"User not found")   

    return getMyProfileService(db, db_author)

def updateAuthorController(db,author,Auth_head,id,role):
    author_id = decode_token_id(Auth_head, model=AuthorToken, db=db)
    if id != None:
        if role == "admin":
            db_author = db.query(Author).filter(Author.Author_id == id).first()
        else:
            errorhandler(403, "You can't update others account")
    else:
        db_author = db.query(Author).filter(Author.Author_id == author_id).first()
        print(db_author.username)
    if db_author == None:
         errorhandler(404, "author not found")
    if db_author != None:
        if validation.User_delete_validation(db_author):
            errorhandler(400, "author not found")
    if author.email:
        if not validation.email_validations(author.email):
            errorhandler(400, "Invalid email")
    if author.phone_number:
        if not validation.phoneNumber_validation(author.phone_number):
            errorhandler(400,"Invalid phone number")
    if author.password:
        if not validation.password_validation(author.password):
            errorhandler(400, "Password should contain 8 character, atleast 1 uppercase letter, atleast 1 lowercase letter, atleast 1 symbol")
    return updateAuthorService(db,author,db_author)

def logoutAuthorController(db,Auth_head,id,role):
    if role != "author":
        admin_id = decode_token_id(Auth_head, model=AdminToken, db=db)
        if id == None:
                errorhandler(400, "admin must use id to logout author")
    if role != "admin":
        author_id = decode_token_id(Auth_head, model=AuthorToken, db=db)
        if id != None:
                errorhandler(403, "author can't logout another author")
    if id != None:
        db_author = db.query(Author).filter(Author.Author_id == id).first()
        if db_author == None:
                errorhandler(404, "author not found")
    else:
        db_author = db.query(Author).filter(Author.Author_id == author_id).first()
            
    if validation.User_delete_validation(db_author):
            errorhandler(404,"author not found")   
    if db_author.is_active == False:
            errorhandler(400, f"{id} is not loggedin yet")

    return signoutAuthorService(db, db_author)

def deleteAuthorController(db,Auth_head,id,role):
    if id != None:
        if role == "admin":
            admin_id = decode_token_id(Auth_head, model=AdminToken, db=db)
            db_author = db.query(Author).filter(Author.Author_id == id).first()
        else:
            errorhandler(400,"You can't delete another acoount")
    else:
        author_id = decode_token_id(Auth_head, model=AuthorToken, db=db)
        db_author = db.query(Author).filter(Author.Author_id == author_id).first()
    if db_author == None:
        errorhandler(404,"author not found")
        print(db_author, "author")
    if validation.User_delete_validation(db_author):
        errorhandler(404,"author not found")   
    return deleteAuthorService(db, db_author)