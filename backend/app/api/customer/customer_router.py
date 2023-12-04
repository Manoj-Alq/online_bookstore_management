from configuration.config import *
from utils.auth import AdminJWT
from sqlalchemy.orm import Session
from .customer_controller import *
from .customer_schema import *
from utils.auth_handlers import *

httpbearer = AdminJWT()

@router.get("/customer/getAllcustomer", tags=['customer'])
async def getAllcustomer(db: Session = Depends(get_session)):
    return getAllcustomerController(db)

@router.get("/customer/getacustomer/{id}", response_model=CustomerResponse, tags=["customer"], summary= "Get single customer")
async def getSinglecustomer(id:int,db: Session = Depends(get_session)):
    return getSinglecustomerController(db,id)

@router.post("/customer/createcustomer", response_model=CustomerResponse, tags=["customer"], summary="customer can signup here")
async def signupcustomer(customer: CustomerSignUp,db: Session = Depends(get_session)):
    return signupcustomerController(db, customer)

@router.post("/customer/loginincustomer/",  tags=["customer"], summary="customers can signin here")
async def logIncustomer(customer: CustomerLogIn,Auth_head:str = Depends(get_authorization_header),db: Session = Depends(get_session)):
    return logIncustomerController(db,customer)

@router.get("/customer/getMyProfile/",dependencies = [Depends(httpbearer)], response_model=CustomerResponse, tags=["customer"], summary="customer can fetch their own profile here")
async def getMyProfile(Auth_head:str = Depends(get_authorization_header),role:str = Depends(customer_authorization),db: Session = Depends(get_session)):
    if role == "customer":    
        return getMyProfileController(db,Auth_head)
    else:
        errorhandler(403,"You can't access this route")

@router.put("/customer/updatecustomer",dependencies = [Depends(httpbearer)], response_model=CustomerResponse, tags=["customer"], summary="customer can update their details here")
async def updatecustomer(customer: CustomerSignUp,id:int = None,Auth_head:str = Depends(get_authorization_header),role:str = Depends(customer_admin_authorization),db: Session = Depends(get_session)):
    return updatecustomerController(db,customer,Auth_head,id,role)

@router.post("/customer/logoutcustomer/",dependencies = [Depends(httpbearer)], tags=["customer"], summary="customer can signout here")
async def signoutcustomer(id:int=None,Auth_head:str = Depends(get_authorization_header),role:str = Depends(customer_admin_authorization),db: Session = Depends(get_session)):
    return logoutcustomerController(db,Auth_head,id,role)

@router.delete("/customer/deletecustomer",dependencies = [Depends(httpbearer)], response_model=CustomerResponse, tags=["customer"], summary="customer can delete their account here")
async def deletecustomer(id:int=None,Auth_head:str = Depends(get_authorization_header),role:str = Depends(customer_admin_authorization),db: Session = Depends(get_session)):
    return deletecustomerController(db,Auth_head,id,role)