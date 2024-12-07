from pydantic import BaseModel, EmailStr
from typing import Union

# Shared fields between Create and Update
class UserBase(BaseModel):
    name: str
    email: EmailStr

# Schema for creating a user (includes password)
class UserCreate(UserBase):
    password: str

# Schema for updating a user
class UserUpdate(BaseModel):
    name: Union[str, None] = None
    email: Union[EmailStr, None] = None
    password: Union[str, None] = None

# Schema for returning a user (excludes password)
class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True


"""

orm_mode is only needed when the Pydantic model must handle data from ORM objects, 
typically in response schemas (e.g., UserResponse).
It is not needed in schemas like UserBase, UserCreate, or UserUpdate because:
These schemas handle data from JSON payloads provided by API clients, not from ORM objects.
They are used for input validation, not for reading or serializing ORM data.
Let me know if you need further clarification!

"""