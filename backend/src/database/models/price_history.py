from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey, Numeric
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from uuid import UUID, uuid4

from .base_model import BaseModel


class PriceHistory(BaseModel):
    __tablename__ = "price_history"
    
    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )
    
    product_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("products.id", ondelete="CASCADE"),
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
        default=datetime.now,
        nullable=False,
    )
    
    product = relationship(
        "Product",
        back_populates="price_history"
    )

    # def __repr__(self) -> str:
    #     return (
    #         f"Price for {self.product_id}"
    #         f"  ${self.price}"
    #     )