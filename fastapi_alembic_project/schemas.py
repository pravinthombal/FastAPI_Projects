from pydantic import BaseModel, EmailStr
from typing import Optional

# Base schema for shared fields
class UserBase(BaseModel):
    name: str
    email: EmailStr

# Schema for creating a user
class UserCreate(UserBase):
    password: str

# Schema for updating a user
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

# Schema for returning a user (response)
class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
