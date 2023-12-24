from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import session
from ..db.models import Profile
from ..db.schemas import ProfileCreate


profile_router = APIRouter()


@profile_router.post("/create_profile/", response_model=ProfileCreate)
def create_profile(profile: ProfileCreate, db: Session = Depends(session.get_db)):
    db_profile = Profile(**profile.model_dump())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


@profile_router.get("/profile/{profile_id}", response_model=ProfileCreate)
def get_profile(profile_id: int, db: Session = Depends(session.get_db)):
    db_profile = db.query(Profile).filter(Profile.id == profile_id).first()
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile
