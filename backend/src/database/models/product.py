"""
Product DB model
"""
from datetime import datetime

from sqlalchemy import String, Text, Boolean, DateTime, Numeric
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from uuid import UUID, uuid4

from .base_model import BaseModel


class Product(BaseModel):
    __tablename__ = "products"
    
    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )
    
    retailer: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    
    product_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    
    product_url: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    
    image_url: Mapped[str] = mapped_column(
        Text,
        nullable=True,
    )
    
    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now,
        nullable=False,
    )
    
    price_history = relationship(
        "PriceHistory",
        back_populates="product"
    )
    
    # def __repr__(self) -> str:
    #     return (
    #         f"Product(\n"
    #         f"  Id = {self.id}\n"
    #         f"  Name = {self.product_name}\n"
    #         f"  Retailer = {self.retailer}\n"
    #         f")"
    #     )