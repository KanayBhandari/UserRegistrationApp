from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.environ.get('DB_USER')
PASSWORD = os.environ.get('DB_PASSWORD')
HOSTNAME = os.environ.get('DB_HOST')
PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
SCHEMA_NAME = os.environ.get('SCHEMA_NAME')

# Fetching values from env variables and replacing here to form the database_url
DATABASE_URL = f'postgresql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DB_NAME}?options=-c%20search_path%3D{SCHEMA_NAME}'

engine = create_engine(DATABASE_URL, echo=True)

# Creating a synchronous session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
