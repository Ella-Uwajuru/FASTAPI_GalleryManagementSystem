# Art Gallery Management System API

A FastAPI-based backend system for managing art galleries, exhibitions, artists, and user data.

## Features

- User Management (CRUD operations)
- Artist Profile Management 
- Exhibition Scheduling
- Data Analysis Tools
- Automated Data Generation
- Data Processing & Cleaning

## Tech Stack

- FastAPI
- SQLAlchemy (ORM)
- PostgreSQL
- Pandas (Data Analysis)
- Faker (Test Data Generation)
- Pydantic (Data Validation)

## Installation

1. Clone the repository: https://github.com/Ella-Uwajuru/FASTAPI_GalleryManagementSystem
2. Create and activate virtual environment:
3. Install dependencies:

4. Configure database:
  - Install PostgreSQL
  - Create database named 'art_gallery_db'
  - Update DATABASE_URL in database.py if needed

## Usage

1. Start the server:
uvicorn app.main:app --reload

2. Access API documentation:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

### Users
- GET /users/ - List all users
- POST /users/ - Create new user
- PUT /users/{user_id} - Update user
- DELETE /users/{user_id} - Delete user

### Artists
- GET /artists/ - List all artists
- POST /artists/ - Create new artist
- PUT /artists/{artist_id} - Update artist
- DELETE /artists/{artist_id} - Delete artist

### Exhibitions
- GET /exhibitions/ - List all exhibitions
- POST /exhibitions/ - Create new exhibition
- PUT /exhibitions/{exhibition_id} - Update exhibition
- DELETE /exhibitions/{exhibition_id} - Delete exhibition

### Artworks
- GET /artworks/ - List all artworks
- POST /artworks/ - Create new artwork
- PUT /artworks/{artwork_id} - Update artwork
- DELETE /artworks/{artwork_id} - Delete artwork    

## Data Processing

The system includes tools for:
- Data cleaning and preprocessing
- Feature engineering

## Test Data Generation

The `generate_data.py` script generates a large amount of test data to populate the database. It creates users, artists, and exhibitions.

