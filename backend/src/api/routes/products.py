"""
Endpoints

POST /products
GET /products
GET /products/{id}
DELETE /products/{id}
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database.session import get_db
from database.models import Product, PriceHistory
from schemas.product import ProductCreate, ProductResponse
from services.scrape_service import create_product
from errors import PriceNotFoundException, UnsupportedRetailerException

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
async def post_products(
        payload: ProductCreate,
        db: Session = Depends(get_db),
        status_code = 201,
    ):
    # call the scrape service so that it can scrape the price 
    # and then send the data back to the frontend if valid
    # otherwise return an error response to the frontend 
    try:
        return await create_product(str(payload.url), db)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except PriceNotFoundException:
        raise HTTPException(
            status_code=422,
            detail="Unable to locate product price"
        )
    except UnsupportedRetailerException:
        raise HTTPException(
            status_code=409,
            detail="Retailer is currently not supported"
        )