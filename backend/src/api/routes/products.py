"""
Endpoints

POST /products
GET /products
GET /products/{id}
DELETE /products/{id}
"""
import json

from fastapi import APIRouter, Depends, HTTPException
from redis import Redis
from sqlalchemy import select
from sqlalchemy.orm import Session

from cache.keys import PRODUCT_LIST_KEY
from database.session import get_db, get_redis
from database.models import Product, PriceHistory
from errors import PriceNotFoundException, UnsupportedRetailerException
from schemas.product import ProductCreate, ProductResponse
from services.scrape_service import create_product

router = APIRouter()

@router.get("/products")
async def get_products(
    db: Session = Depends(get_db),
    redis: Redis = Depends(get_redis),
):
    cached = redis.get(PRODUCT_LIST_KEY)
    if cached:
        print("Cache hit")
        data = json.loads(cached)
        return [
            ProductResponse.model_validate(item)
            for item in data
        ]
    else:
        print("Cache miss")

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
    response = [
        ProductResponse(
            id=product.id,
            productName=product.product_name,
            retailer=product.retailer,
            productUrl=product.product_url,
            price=price,
            currency=currency,
            imageUrl=product.image_url 
                if product.image_url 
                else "https://example.com",
        )
        for product, price, currency in ret
    ]
    payload = [
        p.model_dump(mode="json")
        for p in response
    ]
    redis.set(
        PRODUCT_LIST_KEY,
        json.dumps(payload),
        ex=300,
    )
    return response

    
@router.post("/products")
async def post_products(
        payload: ProductCreate,
        db: Session = Depends(get_db),
        redis: Redis = Depends(get_redis),
        status_code = 201,
    ):
    try:
        redis.delete(PRODUCT_LIST_KEY)
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