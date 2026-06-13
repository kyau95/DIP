
from pydantic import BaseModel
from uuid import UUID


class PriceHistoryResponse(BaseModel):
    id: UUID
    retailer: str
    product_name: str