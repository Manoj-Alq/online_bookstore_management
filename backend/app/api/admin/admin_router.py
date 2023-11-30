from .admin_schema import *
from fastapi import Depends
from sqlalchemy.orm import Session
from .admin_controller import *
from typing import List
from utils.auth import *
from configuration.config import *

httpbearer = AdminJWT()

@router.get("/admin/getAlladmin", response_model=List[AdminResponse], tags=["Admin"], summary="Get all admins")
async def getAlladmin(db: Session = Depends(get_session)):
    return getAlladminController(db)
    # return

@router.get("/admin/getaadmin/{id}",dependencies = [Depends(httpbearer)], response_model=AdminResponse, tags=["Admin"], summary= "Get single admin")
async def getSingleadmin(id:int,Auth_head:str = Depends(get_authorization_header),x : str = Depends(admin_authorization),db: Session = Depends(get_session)):
    return getSingleadminController(db,id,Auth_head)
    # return

@router.post("/admin/createadmin",dependencies = [Depends(httpbearer)], response_model=AdminResponse, tags=["Admin"], summary="admin can signup here")
async def signupadmin(admin: AdminSignUp,Auth_head:str = Depends(get_authorization_header),x : str = Depends(admin_authorization),db: Session = Depends(get_session)):
    return signupController(db, admin, Auth_head)
    # return

@router.post("/admin/loginadmin", response_model=AdminResponse, tags=["Admin"], summary="admins can signin here")
async def signinadmin(admin: AdminSignIn,db: Session = Depends(get_session)):
    return signinController(db,admin)
    # return

@router.get("/admin/getMyProfile",dependencies = [Depends(httpbearer)], response_model=AdminResponse, tags=["Admin"], summary="admin can fetch their own profile here")
async def getMyProfile(Auth_head:str = Depends(get_authorization_header),role : str = Depends(admin_authorization),db: Session = Depends(get_session)):
    if role == "admin":
        return getMyProfileController(db,Auth_head)
    else:
        errorhandler(403,"You can't access this route")

@router.put("/admin/updateadmin",dependencies = [Depends(httpbearer)], response_model=AdminResponse, tags=["Admin"], summary="admin can update their details here")
async def updateadmin(id:int,admin: AdminSignUp,Auth_head:str = Depends(get_authorization_header),x : str = Depends(admin_authorization),db: Session = Depends(get_session)):
    return updateadminController(db,admin,Auth_head,id)

@router.post("/admin/logoutadmin",dependencies = [Depends(httpbearer)], tags=["Admin"], summary="admin can signout here")
async def signoutadmin(id:int,Auth_head:str = Depends(get_authorization_header),x : str = Depends(admin_authorization),db: Session = Depends(get_session)):
    return signOutController(db,Auth_head,id)

@router.delete("/admin/deleteadmin",dependencies = [Depends(httpbearer)], response_model=AdminResponse, tags=["Admin"], summary="admin can delete their account here")
async def deleteadmin(id:int,Auth_head:str = Depends(get_authorization_header),x : str = Depends(admin_authorization),db: Session = Depends(get_session)):
    return deleteadminController(db,Auth_head,id)