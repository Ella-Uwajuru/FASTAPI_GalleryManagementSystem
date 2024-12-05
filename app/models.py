from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String)
    hashed_password = Column(String)
    
    artist_profile = relationship("Artist", back_populates="user", uselist=False)

class Artist(Base):
    __tablename__ = "artists"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    bio = Column(String)
    specialization = Column(String)
    
    user = relationship("User", back_populates="artist_profile")
    artworks = relationship("Artwork", back_populates="artist")

class Artwork(Base):
    __tablename__ = "artworks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    artist_id = Column(Integer, ForeignKey("artists.id"))
    exhibition_id = Column(Integer, ForeignKey("exhibitions.id"), nullable=True)
    
    artist = relationship("Artist", back_populates="artworks")
    exhibition = relationship("Exhibition", back_populates="artworks")

class Exhibition(Base):
    __tablename__ = "exhibitions"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    
    artworks = relationship("Artwork", back_populates="exhibition")