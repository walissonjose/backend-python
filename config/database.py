import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

database_url = os.getenv('DATABASE_URL')

engine = create_engine(database_url)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()
