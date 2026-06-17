from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Numeric, Boolean
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from uuid import UUID, uuid4

from .base_model import BaseModel


class Alert(BaseModel):
    __tablename__ = "alerts"
    
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
    
    target_price: Mapped[float] = mapped_column(
        Numeric,
        nullable=False,
    )
    
    enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now,
        nullable=False,
    )
