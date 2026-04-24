import pandas as pd
from .config import BASE_DIR

def load_and_clean_data():
    df = pd.read_csv(BASE_DIR / "Dataset" / "enriched_movies.csv").drop_duplicates()
    
    # Fill NaN values with empty string for text columns
    text_cols = ['Plot', 'Genre', 'Director', 'Actors']
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].fillna('')
    
    # Create a combined 'content' feature
    df['content'] = df['Plot'] + " " + df['Genre'] + " " + df['Director'] + " " + df['Actors']
    
    return df
