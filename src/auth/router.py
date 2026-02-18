from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from .schemas import UserCreate, UserLogin
from .service import create_user_service, login_user_service

router = APIRouter(
    prefix="/auth",
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(user, db)


@router.post("/login", status_code=status.HTTP_200_OK)
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    return login_user_service(user, db)

