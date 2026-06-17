"""
Endpoints:

GET /price_history
"""

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database.session import get_db
from database.models import PriceHistory

router = APIRouter()

@router.get("/price_history")
def get_price_history(db: Session = Depends(get_db)):
    stmt = select(PriceHistory)
    
    price_histories = db.scalars(stmt).all()
    
    return [
        {
            "id": ph.id,
            "productId": ph.product_id,
            "currency": ph.currency,
            "price": ph.price
        }
        for ph in price_histories
    ]