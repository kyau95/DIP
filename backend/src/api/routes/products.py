"""
Endpoints

POST /products
GET /products
GET /products/{id}
DELETE /products/{id}
"""

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from database.session import get_db
from database.models import Product, PriceHistory
from schemas.product import ProductResponse

router = APIRouter()

@router.get("/products")
async def get_products(db: Session = Depends(get_db)):
    latest_price_subquery = (
        select(
            PriceHistory.product_id,
            PriceHistory.price,
            PriceHistory.currency
        ).distinct(PriceHistory.product_id)
        .order_by(
            PriceHistory.product_id,
            PriceHistory.scraped_at.desc()
        ).subquery()
    )
    
    stmt = (
        select(
            Product,
            latest_price_subquery.c.price,
            latest_price_subquery.c.currency,
        )
        .join(
            latest_price_subquery,
            Product.id == latest_price_subquery.c.product_id
        )
    )
    
    ret = db.execute(stmt).all()

    return [
        ProductResponse(
            id=product.id,
            productName=product.product_name,
            retailer=product.retailer,
            productUrl=product.product_url,
            price=price,
            currency=currency,
            imageUrl=product.image_url if product.image_url else "https://example.com",
        )
        for product, price, currency in ret
    ]

    
@router.post("/products")
async def post_products(db: Session = Depends(get_db)):
    pass