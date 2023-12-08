from configuration.config import *
from utils.auth import AdminJWT
from sqlalchemy.orm import Session
from .review_controller import *
from .review_schema import *
from utils.auth_handlers import *

httpbearer = AdminJWT()

@router.get("/review/getAllreview", tags=['Review'])
async def getAllreview(db: Session = Depends(get_session)):
    return getAllreviewController(db)

@router.get("/review/getareview/{id}",response_model=ReveiwResponse, tags=["Review"])
async def getSinglereview(id:int,db: Session = Depends(get_session)):
    return getSinglereviewController(db, id) 

@router.post("/review/createreview",dependencies = [Depends(httpbearer)],response_model=ReveiwResponse, tags=["Review"])
async def createreview(review: CreateReview,role:str = Depends(customer_authorization),Auth_head:str = Depends(get_authorization_header),db: Session = Depends(get_session)):
    return createReviewController(db,review, Auth_head)

@router.post("/review/updatereview",dependencies = [Depends(httpbearer)],response_model=ReveiwResponse, tags=["Review"])
async def updatereview(review: CreateReview,id:int,Auth_head:str = Depends(get_authorization_header),db: Session = Depends(get_session)):
    return updateReviewController(db,review, id, Auth_head)

@router.post("/review/deletereview",dependencies = [Depends(httpbearer)],response_model=ReveiwResponse, tags=["Review"])
async def signupreview(id:int = None,Auth_head:str = Depends(get_authorization_header),db: Session = Depends(get_session)):
    return deletereviewController(db, Auth_head, id)
