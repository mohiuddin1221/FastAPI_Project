from typing import List
import uuid
from datetime import datetime
from sqlalchemy import Identity
from sqlalchemy import String, DateTime, Boolean, func, UUID, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import Enum
from sqlalchemy.orm import relationship
from database import Base
from .choices import UserStatus
from .schemas import UserCreate
from src.product.models import Category, Product


class User(Base):
    __tablename__ = "user_account"

    __pydantic_model__ = UserCreate

    uid: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), index=True, primary_key=True, default=uuid.uuid4
    )
    id: Mapped[int] = mapped_column(
        Integer, Identity(always=False, start=1), unique=True, nullable=False
    )

    firstname: Mapped[str] = mapped_column(String(30))
    lastname: Mapped[str] = mapped_column(String(30))
    username: Mapped[str] = mapped_column(String(30))

    phone_number: Mapped[str] = mapped_column(String(20), nullable=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    status: Mapped[UserStatus] = mapped_column(
        Enum(UserStatus), default=UserStatus.PENDING, nullable=False
    )
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )

    categories: Mapped[List["Category"]] = relationship(
        "Category", back_populates="user", cascade="all, delete-orphan"
    )
    products: Mapped[List["Product"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"User{self.id}-- {self.username}"

    @hybrid_property
    def total_categories(self):
        return len(self.categories)

        
    @hybrid_property
    def total_products(self):
        return len(self.products)
