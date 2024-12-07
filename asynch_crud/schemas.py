from pydantic import BaseModel, EmailStr
from typing import Optional

# Shared User schema
class UserBase(BaseModel):
    name: str
    email: EmailStr

# Create schema with password
class UserCreate(UserBase):
    password: str

# Response schema without password
class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True

# Update schema
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
