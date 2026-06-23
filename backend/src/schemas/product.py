"""
Pydantic model for products 
"""
from pydantic import BaseModel, HttpUrl
from uuid import UUID


class ProductResponse(BaseModel):
    id: UUID
    imageUrl: str
    price: float
    currency: str
    productName: str
    productUrl: str
    retailer: str
    

class ProductCreate(BaseModel):
    url: HttpUrl