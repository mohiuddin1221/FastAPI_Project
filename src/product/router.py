from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from .schemas import Category, CategoryListResponse
from src.auth.models import User
from src.auth.oauth2 import get_current_user
from .service import create_category_service, category_service

router = APIRouter(
    prefix="/product",
)


@router.post("/category", status_code=status.HTTP_201_CREATED)
async def create_category(category: Category, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_category_service(category, db, current_user)

@router.get("/category", response_model=CategoryListResponse)
async def get_categories(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return category_service(db, current_user)