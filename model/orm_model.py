from datetime import datetime
from decimal import Decimal

from sqlalchemy import Integer, String, DateTime, func, Float, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.database import Base


class Category(Base):

    __tablename__ = 'category'

    category_id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    category_code : Mapped[str] = mapped_column(String, index=True, unique=True)
    category_name : Mapped[str] = mapped_column(String, nullable=False)
    description : Mapped[str] = mapped_column(String, nullable=True)
    active : Mapped[str] = mapped_column(String, nullable=False)

    product_id: Mapped["Product"] = relationship(
        back_populates="category",

    )

class Product(Base):

    __tablename__ = 'product'

    product_id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    category : Mapped[Category] = mapped_column(
        ForeignKey("category.category_id", ondelete="CASCADE"), nullable=False,
    )
    product_code : Mapped[str] = mapped_column(String, index=True, unique=True)
    product_name : Mapped[str] = mapped_column(String, nullable=False)
    unit_price : Mapped[Decimal] = mapped_column(nullable=False)
    available_quantity : Mapped[int] = mapped_column(Integer, nullable=False)
    active: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    category_id : Mapped[Category] = relationship(
        back_populates="product",

    )

class LoyaltyCustomer(Base):

    __tablename__ = 'loyalty_customer'

    id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    mobile_number : Mapped[str] = mapped_column(String, nullable=False, unique=True)
    full_name : Mapped[str] = mapped_column(String, nullable=False)
    email : Mapped[str] = mapped_column(String, nullable=True)
    loyalty_points : Mapped[float] = mapped_column(Float)
    registered_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

class Oder(Base):

    __tablename__ = 'order'

    id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id : Mapped[Category] = mapped_column(
        ForeignKey("loyalty_customer.customer_id", ondelete="CASCADE"), nullable=False,
    )
    order_date_time : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    order_status : Mapped[str] = mapped_column(String, default="PENDING", nullable=False)
    total_amount : Mapped[Decimal] = mapped_column(Numeric, nullable=False)
    loyalty_points : Mapped[float] = mapped_column(Float, default=0)


class OderItem(Base):

    __tablename__ = 'order_item'

    order_item_id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id : Mapped[Oder] = mapped_column(
        ForeignKey("order.order_id", ondelete="CASCADE"), nullable=False,
    )
    product_id : Mapped[Product] = mapped_column(
        ForeignKey("product.product_id", ondelete="CASCADE"), nullable=False,
    )
    quantity : Mapped[int] = mapped_column(Integer, nullable=False)
    unit_price : Mapped[Decimal] = mapped_column(nullable=False)
    subtotal : Mapped[Decimal] = mapped_column(nullable=False)