from pydantic import BaseModel

class UserBase(BaseModel):
    full_name: str
    email: str
    phone: str

class UserCreate(UserBase):
    password: str
    profile_picture_url: str

class UserResponse(UserBase):
    id: int
    profile_picture_url: str

class ProfileCreate(BaseModel):
    profile_picture_url: str
