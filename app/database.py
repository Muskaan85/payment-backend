import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("DATABASE_URL")  

if not DATABASE_URL:
    # Fallback for local dev
    DATABASE_URL = "mysql+pymysql://root:GUlMQWsguxtsEyNhjJPbGFYwbwKGGubL@hopper.proxy.rlwy.net:31555/railway"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Create tables if not exist
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
