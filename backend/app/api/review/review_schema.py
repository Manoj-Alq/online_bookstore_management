from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class ReveiwResponse(BaseModel):
    review_id : int = None
    book_id : int = None
    customer_id : int = None
    review_points : float = None
    review_comment : str = None
    created_at : Optional[datetime]
    created_by : int = None
    updated_at : Optional[datetime]
    updated_by : int = None
    
class CreateReview(BaseModel):
    book_id : int = None
    review_points : float = None
    review_comment : str = None

