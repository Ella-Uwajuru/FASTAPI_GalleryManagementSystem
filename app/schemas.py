from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

class UserBase(BaseModel):
    email: Optional[str] = None
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        from_attributes = True

class ArtistBase(BaseModel):
    bio: Optional[str] = None
    specialization: Optional[str] = None

class ArtistCreate(ArtistBase):
    user_id: int

class Artist(ArtistBase):
    id: int
    user_id: int
    class Config:
        from_attributes = True

class ArtworkBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: Optional[float] = None

class ArtworkCreate(ArtworkBase):
    artist_id: int

class Artwork(ArtworkBase):
    id: int
    artist_id: int
    exhibition_id: Optional[int] = None
    class Config:
        from_attributes = True

class ExhibitionBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime

class ExhibitionCreate(ExhibitionBase):
    pass

class Exhibition(ExhibitionBase):
    id: int
    class Config:
        from_attributes = True