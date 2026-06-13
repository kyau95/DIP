
from pydantic import BaseModel
from uuid import UUID


class ProductResponse(BaseModel):
    id: UUID
    retailer: str
    product_name: str