from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, database

# Create tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User endpoints
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(email=user.email, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

# Artist endpoints
@app.post("/artists/", response_model=schemas.Artist)
def create_artist(artist: schemas.ArtistCreate, db: Session = Depends(get_db)):
    db_artist = models.Artist(**artist.model_dump())
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

@app.get("/artists/", response_model=List[schemas.Artist])
def read_artists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    artists = db.query(models.Artist).offset(skip).limit(limit).all()
    return artists

# Artwork endpoints
@app.post("/artworks/", response_model=schemas.Artwork)
def create_artwork(artwork: schemas.ArtworkCreate, db: Session = Depends(get_db)):
    db_artwork = models.Artwork(**artwork.model_dump())
    db.add(db_artwork)
    db.commit()
    db.refresh(db_artwork)
    return db_artwork

@app.get("/artworks/", response_model=List[schemas.Artwork])
def read_artworks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    artworks = db.query(models.Artwork).offset(skip).limit(limit).all()
    return artworks

# Exhibition endpoints
@app.post("/exhibitions/", response_model=schemas.Exhibition)
def create_exhibition(exhibition: schemas.ExhibitionCreate, db: Session = Depends(get_db)):
    db_exhibition = models.Exhibition(**exhibition.model_dump())
    db.add(db_exhibition)
    db.commit()
    db.refresh(db_exhibition)
    return db_exhibition

@app.get("/exhibitions/", response_model=List[schemas.Exhibition])
def read_exhibitions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    exhibitions = db.query(models.Exhibition).offset(skip).limit(limit).all()
    return exhibitions