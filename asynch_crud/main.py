from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from database import engine, Base, get_db
from crud import get_user, get_users, create_user, update_user, delete_user, get_user_by_email
from schemas import UserCreate, UserUpdate, UserOut

app = FastAPI()

# Initialize database
@app.on_event("startup")   # on_event ,    lifespan
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Routes
@app.get("/users/", response_model=List[UserOut])
async def read_users(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await get_users(db, skip, limit)

@app.get("/users/{user_id}", response_model=UserOut)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users/", response_model=UserOut)
async def create_new_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await create_user(db, user)

@app.put("/users/{user_id}", response_model=UserOut)
async def update_existing_user(user_id: int, user: UserUpdate, db: AsyncSession = Depends(get_db)):
    updated_user = await update_user(db, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/users/{user_id}", response_model=UserOut)
async def delete_existing_user(user_id: int, db: AsyncSession = Depends(get_db)):
    deleted_user = await delete_user(db, user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user
