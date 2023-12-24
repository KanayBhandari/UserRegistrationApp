from fastapi import FastAPI
from dotenv import load_dotenv
from app.api.user import user_router
from app.api.profiles import profile_router
from app.db.models import Base
from app.db.session import engine

# Load all env variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include your API routers
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(profile_router, prefix="/profiles", tags=["profiles"])