from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQL database URL
# DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/mydatabase"
DATABASE_URL = "mysql+pymysql://root:@localhost/practice_pymysql"

# Create the database engine
engine = create_engine(DATABASE_URL)

# SessionLocal to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base for models
Base = declarative_base()

