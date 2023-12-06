from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List
from utils.auth import *
from configuration.config import *
from .cart_schema import *
from .cart_controller import *

httpbearer = AdminJWT()

@router.get("/cart/getAllcart",response_model=List[cartresponse], tags=["Cart"])
async def getAllcart(db: Session = Depends(get_session)):
    return getAllcartController(db)

@router.get("/cart/getacart/{id}",response_model=cartresponse, tags=["Cart"])
async def getSinglecart(id:int,db: Session = Depends(get_session)):
    return getSinglecartController(db, id) 

@router.post("/cart/createcart",dependencies = [Depends(httpbearer)],response_model=cartresponse, tags=["Cart"])
async def createcart(cart: create_cart,role:str = Depends(customer_authorization),Auth_head:str = Depends(get_authorization_header),db: Session = Depends(get_session)):
    return createcartController(db,cart, Auth_head)

@router.post("/cart/updatecart",dependencies = [Depends(httpbearer)],response_model=cartresponse, tags=["Cart"])
async def updatecart(cart: create_cart,id:int,Auth_head:str = Depends(get_authorization_header),db: Session = Depends(get_session)):
    return updatecartController(db,cart, id)

@router.post("/cart/deletecart",dependencies = [Depends(httpbearer)],response_model=cartresponse, tags=["Cart"])
async def signupcart(id:int = None,Auth_head:str = Depends(get_authorization_header),db: Session = Depends(get_session)):
    return deletecartController(db, Auth_head, id)

@router.post("/buyBooks",dependencies = [Depends(httpbearer)], tags=["Cart"])
async def create_order(role:str = Depends(customer_authorization),Auth_head:str = Depends(get_authorization_header),db: Session = Depends(get_session)):
    return buyBooksController(db,Auth_head)