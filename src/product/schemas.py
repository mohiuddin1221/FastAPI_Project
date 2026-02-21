from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Category(BaseModel):
    title: str
    description: Optional[str] = Field(default=None)


class CategoryResponse(BaseModel):
    id: int
    uid: UUID
    title: str
    description: Optional[str] = Field(default=None)
    user_id: UUID
    created_at: datetime
    updated_at: datetime



class CategoryListResponse(BaseModel):
    total: int
    categories: list[CategoryResponse]

    class Config:
        orm_mode = True


class Product(BaseModel):
    title: str
    description: Optional[str] = Field(default=None)
    price: float
    stock: int
    category_id: UUID

class ProductResponse(BaseModel):
    total_products: int
    products: list[Product]