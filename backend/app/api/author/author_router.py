from configuration.config import *
from utils.auth import AdminJWT
from sqlalchemy.orm import Session
from .author_controller import *
from .author_schema import *
from utils.auth_handlers import *

httpbearer = AdminJWT()

@router.get("/author/getAllAuthor", tags=['Author'])
async def getAllAuthor(db: Session = Depends(get_session)):
    return getAllAuthorController(db)

@router.get("/author/getaAuthor/{id}", response_model=AuthorResponse, tags=["Author"], summary= "Get single author")
async def getSingleauthor(id:int,db: Session = Depends(get_session)):
    return getSingleauthorController(db,id)

@router.post("/author/createauthor", response_model=AuthorResponse, tags=["Author"], summary="author can signup here")
async def signupauthor(author: AuthorSignUp,db: Session = Depends(get_session)):
    return signupAuthorController(db, author)

@router.post("/author/logininauthor/",  tags=["Author"], summary="authors can signin here")
async def logInauthor(author: AuthorLogIn,Auth_head:str = Depends(get_authorization_header),db: Session = Depends(get_session)):
    return logInAuthorController(db,author)

@router.get("/author/getMyProfile/",dependencies = [Depends(httpbearer)], response_model=AuthorResponse, tags=["Author"], summary="author can fetch their own profile here")
async def getMyProfile(Auth_head:str = Depends(get_authorization_header),role:str = Depends(author_authorization),db: Session = Depends(get_session)):
    if role == "author":
        return getMyProfileController(db,Auth_head)
    else:
        errorhandler(403,"You can't access this route")

@router.put("/author/updateauthor",dependencies = [Depends(httpbearer)], response_model=AuthorResponse, tags=["Author"], summary="author can update their details here")
async def updateauthor(author: AuthorSignUp,id:int = None,Auth_head:str = Depends(get_authorization_header),role:str = Depends(author_authorization),db: Session = Depends(get_session)):
    return updateAuthorController(db,author,Auth_head,id,role)

@router.post("/author/logoutAuthor/",dependencies = [Depends(httpbearer)], tags=["Author"], summary="Author can signout here")
async def signoutauthor(id:int=None,Auth_head:str = Depends(get_authorization_header),role:str = Depends(author_authorization),db: Session = Depends(get_session)):
    return logoutAuthorController(db,Auth_head,id,role)

@router.delete("/author/deleteauthor",dependencies = [Depends(httpbearer)], response_model=AuthorResponse, tags=["Author"], summary="author can delete their account here")
async def deleteauthor(id:int=None,Auth_head:str = Depends(get_authorization_header),role:str = Depends(author_admin_authorization),db: Session = Depends(get_session)):
    return deleteAuthorController(db,Auth_head,id,role)