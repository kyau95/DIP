"""
Endpoints

POST /products
GET /products
GET /products/{id}
DELETE /products/{id}
"""

from fastapi import APIRouter


router = APIRouter()

@router.get("/products")
def get_products():
    return [
        {
            "id": 1,
            "productName": "RTX 5090",
            "price": 549.99,
            "url": "https://example.com",
            "currency": "$"
        }
    ]