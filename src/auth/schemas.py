from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserBase(BaseModel):
    firstname: str
    lastname: str
    username: str
    email: EmailStr
    phone_number: Optional[str] = Field(default=None)

class UserCreate(UserBase):
    password: str
    
    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None

