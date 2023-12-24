from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import session
from ..db.models import User, Profile
from ..db.schemas import UserCreate, UserResponse, ProfileCreate
from ..core.security import hash_password


user_router = APIRouter()


@user_router.post("/register/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(session.get_db)):
    # Check if the email is already registered
    existing_user_email = db.query(User).filter(User.email == user.email).first()
    if existing_user_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Check if the phone is already registered
    existing_user_phone = db.query(User).filter(User.phone == user.phone).first()
    if existing_user_phone:
        raise HTTPException(status_code=400, detail="Phone number already registered")

    password = hash_password(user.password)

    user.password = password
    profile_picture = user.profile_picture_url
    del user.profile_picture_url

    db_user = User(**user.model_dump())
    db.add(db_user)

    db.commit()
    db.refresh(db_user)

    profile = ProfileCreate(profile_picture_url=profile_picture)
    db_profile = Profile(**profile.model_dump(), user_id=db_user.id)
    db.add(db_profile)

    db.commit()
    db.refresh(db_profile)

    # deleting the password since that is not needed in response
    del user.password
    return {"id": db_user.id, **user.model_dump(), "profile_picture_url": profile_picture}


@user_router.get("/user/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(session.get_db)):
    user = db.query(User).filter(User.id == user_id).join(Profile).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(id=user.id, full_name=user.full_name,
                        email=user.email, phone=user.phone,
                        profile_picture_url=user.profile.profile_picture_url)
