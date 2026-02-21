import uuid
from typing import List
from datetime import datetime
from sqlalchemy import Identity
from sqlalchemy import String, DateTime, Boolean, func, UUID, Integer,Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy import Enum
from database import Base
from sqlalchemy.orm import relationship
from .schemas import CategoryResponse



class Category(Base):
    __tablename__ = "category"


    __pydantic_model__ = CategoryResponse

    uid: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), index=True, primary_key=True, default=uuid.uuid4
    )
    id: Mapped[int] = mapped_column(
        Integer, Identity(always=False, start=1), unique=True, nullable=False
    )

    title: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(30))

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user_account.uid"))

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )
    user: Mapped["User"] = relationship("User", back_populates="categories")
    products: Mapped[List["Product"]] = relationship(back_populates="category")

    def __repr__(self):
        return f"Category{self.id}-- {self.title}"


class Product(Base):
    __tablename__ = "product"
    
    uid: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), index=True, primary_key=True, default=uuid.uuid4
    )
    id: Mapped[int] = mapped_column(
        Integer, Identity(always=False, start=1), unique=True, nullable=False
    )

    title: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(500))
    price: Mapped[float] = mapped_column(Float)
    stock: Mapped[int] = mapped_column(Integer)


    #FK
    category_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("category.uid"))
    category: Mapped["Category"] = relationship(back_populates="products")

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user_account.uid"))
    user: Mapped["User"] = relationship(back_populates="products")

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        return f"Product{self.title}"