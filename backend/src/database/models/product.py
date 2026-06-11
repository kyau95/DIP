from datetime import datetime

from sqlalchemy import String, Text, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from uuid import UUID, uuid4

from database.models.base_model import BaseModel


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
        default=datetime.utcnow,
        nullable=False,
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )