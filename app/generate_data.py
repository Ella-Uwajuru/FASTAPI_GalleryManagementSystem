from faker import Faker
import random
from datetime import timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Artist, Artwork, Exhibition


fake = Faker()
fake.seed_instance(12345)


engine = create_engine("postgresql://postgres:123@localhost:5432/art_gallery_db")
SessionLocal = sessionmaker(bind=engine)

def generate_data():
    db = SessionLocal()
    
    try:
        # Clear existing data
        for table in [Artwork, Exhibition, Artist, User]:
            db.query(table).delete()
        db.commit()

       
        print("Generating users...")
        users = []
        for _ in range(200000):
            username = fake.unique.user_name()
            if random.random() < 0.1:
                email = None 
            else:
                email = fake.unique.email()
            
            users.append(User(
                email=email,
                username=username,
                hashed_password=fake.password(length=60)
            ))
        db.add_all(users)
        db.commit()

       
        print("Generating artists...")
        artists = []
        specializations = ['Painting', 'Sculpture', 'Photography', 'Digital Art', None]
        artist_users = random.sample(users, k=100000)
        
        for user in artist_users:
            artists.append(Artist(
                user_id=user.id,
                bio=fake.text() if random.random() > 0.2 else None,
                specialization=random.choice(specializations)
            ))
        db.add_all(artists)
        db.commit()

        print("Generating exhibitions...")
        exhibitions = []
        for _ in range(200000):
            start_date = fake.date_time_this_year()
            exhibitions.append(Exhibition(
                title=fake.catch_phrase(),
                description=fake.text() if random.random() > 0.3 else None,
                start_date=start_date,
                end_date=start_date + timedelta(days=random.randint(1, 90))
            ))
        db.add_all(exhibitions)
        db.commit()

        print("\nData generation completed!")

    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    generate_data()