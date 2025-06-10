from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import EmailStr

class UserBase(SQLModel):
    name: str = Field(index=True, unique=True)
    email: EmailStr = Field(index=True, unique=True)
    role: str = Field(default="client")  

class User(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)
    hashed_password: str
    refresh_token: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
