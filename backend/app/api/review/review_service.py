from .review_models import *
from utils.handlers import *
from utils.auth_handlers import *
from fastapi.responses import JSONResponse
from datetime import datetime
from api.cart.cart_model import Sales

def getAllreviewService(db):
    try:
        db_reviews = db.query(Review).filter(Review.is_deleted == False).all()
        return db_reviews
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def getSinglereviewService(db,db_review):
    try:
        return db_review
    except Exception as e:
        db.rollback()
        errorhandler(400,f"{e}")

def createReviewService(db, review,customer_id):
    try:
        db_review = Review(
            book_id = review.book_id,
            review_points = review.review_points,
            review_comment = review.review_comment,
            customer_id = customer_id,
            created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            created_by = customer_id
        )
        db.add(db_review)
        db.commit()
        db.refresh(db_review)

        return JSONResponse({
            "message":"review created successfully"
        })
    
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def updateReviewservice(db,db_review,review, customer_id):
    try:
        if review.review_points != "" and review.review_points != None:
                db_review.review_points = review.review_points
        if review.review_comment != "" and review.review_comment != None:
                db_review.review_comment = review.review_comment
        db_review.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db_review.updated_by = customer_id
        db.commit()

        return JSONResponse({
            "message":"review updated successfully"
        })
    
    except Exception as e:
        db.rollback()
        errorhandler(400, f"{e}")

def deleteReviewService(db,db_review):
    try:
        db_review.is_deleted = True
        db.commit()
        return JSONResponse({
            "message":"cart deleted successfully"
        })
    except Exception as e:
        db.rollback()
        errorhandler(400,f"{e}")