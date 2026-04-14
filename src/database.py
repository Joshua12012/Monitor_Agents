from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(
   url=os.getenv("DATABASE_URL"),
    echo=False,
    pool_pre_ping=True,          # Important for Neon (wakes up sleeping DB)
    connect_args={
        "connect_timeout": 15,
        "sslmode": "require"
    }
)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
