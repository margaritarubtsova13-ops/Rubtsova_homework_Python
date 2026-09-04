from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "postgresql://postgres:<YOUR_PASSWORD>@localhost:5432/QA"

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


def get_db() -> Session:
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
