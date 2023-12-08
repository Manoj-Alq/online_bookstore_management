from .review_service import *
from utils.validations import Validations

validation = Validations()

def getAllreviewController(db):
    return getAllreviewService(db)

def getSinglereviewController(db, id):
    db_review = db.query(Review).filter(Review.review_id == id, Review.is_deleted == False).first()
    if db_review is None:
        errorhandler(404,"review not found")
    return getSinglereviewService(db,db_review) 

def createReviewController(db,review, Auth_head):
    customer_id  = decode_token_id(Auth_head)
    if validation.None_validation(review.review_points, review.review_comment):
        errorhandler(400, "All field's are required")
    if validation.empty_validation(review):
        key = validation.empty_key_validation(review)
        errorhandler(400, f"{key} shouldn't be empty")
    db_sales = db.query(Sales).filter(Sales.customer_id == customer_id).all()
    if db_sales == []:
        errorhandler(400," you cant review to this book")
    for i in db_sales:
        if review.book_id not in i.book_id:
            errorhandler(400," you cant review to this book")
    print(db_sales)
    return createReviewService(db, review,customer_id)

def updateReviewController(db,review, id, Auth_head):
    customer_id  = decode_token_id(Auth_head)
    db_review = db.query(Review).filter(Review.review_id == id, Review.is_deleted == False).first()
    if db_review.customer_id != customer_id:
        errorhandler(403, " you cant update this review")
    if db_review == None:
        errorhandler(404, "book not found")
    return updateReviewservice(db,db_review,review,customer_id)

def deletereviewController(db, Auth_head, id):
    customer_id  = decode_token_id(Auth_head)
    db_review = db.query(Review).filter(Review.review_id == id, Review.is_deleted == False).first()
    print(db_review)
    if db_review == None:
        errorhandler(404, "review not found")
    if db_review.customer_id != customer_id:
        errorhandler(403, " you cant delete this review")
    
    return deleteReviewService(db,db_review)
