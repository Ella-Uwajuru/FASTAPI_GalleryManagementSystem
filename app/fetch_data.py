import requests
import pandas as pd

BASE_URL = "http://127.0.0.1:8000"

def fetch_data():
    """Fetch data from endpoints"""
    try:
        # Fetch data from each endpoint
        users = requests.get(f"{BASE_URL}/users/").json()
        artists = requests.get(f"{BASE_URL}/artists/").json()
        exhibitions = requests.get(f"{BASE_URL}/exhibitions/").json()

        print("\n=== Data Fetched Successfully ===")
        print(f"Total Users: {len(users)}")
        print(f"Total Artists: {len(artists)}")
        print(f"Total Exhibitions: {len(exhibitions)}")

        return users, artists, exhibitions

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None, None, None

def analyze_data(users, artists, exhibitions):
    """Basic data analysis"""
    try:
      
        df_users = pd.DataFrame(users)
        df_artists = pd.DataFrame(artists)
        df_exhibitions = pd.DataFrame(exhibitions)

        print("\n=== Basic Analysis ===")
      
        if not df_users.empty:
            print("\nUser Statistics:")
            print(f"Number of users with email: {df_users['email'].notna().sum()}")
            
       
        if not df_artists.empty:
            print("\nArtist Specializations:")
            print(df_artists['specialization'].value_counts())
       
        if not df_exhibitions.empty:
            print("\nExhibition Dates:")
            df_exhibitions['start_date'] = pd.to_datetime(df_exhibitions['start_date'])
            print(f"Earliest exhibition: {df_exhibitions['start_date'].min()}")
            print(f"Latest exhibition: {df_exhibitions['start_date'].max()}")

    except Exception as e:
        print(f"Error analyzing data: {e}")

def main():
   
    users, artists, exhibitions = fetch_data()
    
    if users:
      
        analyze_data(users, artists, exhibitions)

if __name__ == "__main__":
    main()