from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL database URL
DATABASE_URL = "mysql+pymysql://root:@localhost/practice_pymysql"

# SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
