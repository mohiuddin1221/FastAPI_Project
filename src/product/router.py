from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db

from src.auth.models import User
from src.auth.oauth2 import get_current_user
from .service import create_category_service, category_service,create_product_service, product_service, category_with_count_service
from .schemas import Category, CategoryListResponse, Product, ProductResponse

router = APIRouter(
    prefix="/product",
)


@router.post("/category", status_code=status.HTTP_201_CREATED)
async def create_category(
    category: Category,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_category_service(category, db, current_user)


@router.get("/category", response_model=CategoryListResponse)
async def get_categories(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return category_service(db, current_user)


@router.post("/product", status_code=status.HTTP_201_CREATED)
async def create_product(
    product: Product,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_product_service(product, db, current_user)

@router.get("/product", response_model=ProductResponse)
async def get_products(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return product_service(db, current_user)


@router.get("/categories-with-count")
async def get_categories_with_count(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return category_with_count_service(db, current_user)