from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.auth.models import User
from .utils import hash_password, verify_password
from .oauth2 import create_access_token, create_refresh_token


def create_user_service(user_data, db):
    stmt = select(User).where(User.email == user_data.email)
    result = db.execute(stmt)
    existing_user = result.scalars().first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email Exist"
        )
    user_data.password = hash_password(user_data.password)

    New_user = User(**user_data.model_dump())

    try:
        db.add(New_user)
        db.commit()
        db.refresh(New_user)
        return New_user
    except Exception as e:
        print(f"Error logic: {e}")
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def login_user_service(user_data, db):
    stmt = select(User).where(User.email == user_data.email)
    result = db.execute(stmt)
    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found"
        )
    if not verify_password(user_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials"
        )

    access_token = create_access_token({"user_id": str(user.uid)})
    refresh_token = create_refresh_token(data={"user_id": str(user.uid)})
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }
