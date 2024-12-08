from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+aiomysql://root:@localhost/practice_pymysql"

# Async SQLAlchemy engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Session factory
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base class for models
Base = declarative_base()

# Dependency
async def get_db():
    async with async_session() as session:
        yield session
