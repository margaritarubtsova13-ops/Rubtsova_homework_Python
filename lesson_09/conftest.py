import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# ВАЖНО: Замени 'ТВОЙ_ПАРОЛЬ' на реальный пароль от postgres!
DATABASE_URL = "postgresql://postgres:1122334456@localhost:5432/QA"

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
