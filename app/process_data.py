import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.preprocessing import StandardScaler

# Database connection
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123@localhost:5432/art_gallery_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

def load_data():
    queries = {
        'users': "SELECT * FROM users",
        'artists': "SELECT * FROM artists",
        'exhibitions': "SELECT * FROM exhibitions"
    }
    
    dataframes = {}
    for name, query in queries.items():
        df = pd.read_sql(query, engine)
        dataframes[name] = df
    
    return dataframes

def describe_datasets(dataframes):
    for name, df in dataframes.items():
        print(f"\n=== {name.upper()} ===")
        print(f"Shape: {df.shape}")
        print("\nData Types:")
        print(df.dtypes)
        print("\nNull Values:")
        print(df.isnull().sum())
        print("\nSummary Statistics:")
        print(df.describe())

def handle_nulls(dataframes):
    clean_dfs = {}
    
    for name, df in dataframes.items():
        df_clean = df.copy()
        
        numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            df_clean[col].fillna(df_clean[col].mean(), inplace=True)
        
        categorical_cols = df_clean.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)
            
        clean_dfs[name] = df_clean
        
    return clean_dfs

def process_data(dataframes):
    processed_dfs = {}
    
    for name, df in dataframes.items():
        df_processed = df.copy()
        
        df_processed.drop_duplicates(inplace=True)
        
        numeric_cols = df_processed.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            scaler = StandardScaler()
            df_processed[numeric_cols] = scaler.fit_transform(df_processed[numeric_cols])
        
        processed_dfs[name] = df_processed
        
    return processed_dfs

def create_features(dataframes):
    enhanced_dfs = {}
    
    if 'exhibitions' in dataframes:
        df = dataframes['exhibitions'].copy()
        df['duration'] = (df['end_date'] - df['start_date']).dt.days
        df['season'] = df['start_date'].dt.month.map({
            12: 'Winter', 1: 'Winter', 2: 'Winter',
            3: 'Spring', 4: 'Spring', 5: 'Spring',
            6: 'Summer', 7: 'Summer', 8: 'Summer',
            9: 'Fall', 10: 'Fall', 11: 'Fall'
        })
        enhanced_dfs['exhibitions'] = df
    
    return enhanced_dfs

def main():
    print("Loading data...")
    dataframes = load_data()
    
    print("\nDescribing datasets...")
    describe_datasets(dataframes)
    
    print("\nHandling null values...")
    clean_dfs = handle_nulls(dataframes)
    
    print("\nProcessing data...")
    processed_dfs = process_data(clean_dfs)
    
  
    print("\nCreating new features...")
    enhanced_dfs = create_features(processed_dfs)
    
   
    print("\nSaving processed data...")
    for name, df in enhanced_dfs.items():
        df.to_csv(f'processed_{name}.csv', index=False)
        print(f"Saved {name} to processed_{name}.csv")

if __name__ == "__main__":
    main()