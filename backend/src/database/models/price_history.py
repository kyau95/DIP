from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from uuid import UUID, uuid4

from database.models.base_model import BaseModel


class PriceHistory(BaseModel):
    __tablename__ = "price_history"
    
    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )
    
    product_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("products.id"),
        nullable=False,
    )
    
    price: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )
    
    currency: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )
    
    stock_status: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )
    
    scraped_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )
