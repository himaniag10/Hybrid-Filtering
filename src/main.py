import sys
import pandas as pd
from pathlib import Path

# Ensure src is in pythonpath
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.data_loader import load_and_clean_data
from src.features import engineer_features
from src.recommend import get_recommendations

def main():
    print("=" * 50)
    print("Starting Content-Based NLP Recommendation Pipeline...")
    print("=" * 50)
    
    print("\n1. Loading Enriched Data...")
    df = load_and_clean_data()
    print(f"Loaded {len(df)} movies.")
    
    print("\n2. Engineering TF-IDF Features...")
    cosine_sim = engineer_features(df)
    
    print("\n3. Running Sample Recommendations...")
    seed_movie = "Toy Story"
    print(f"\nTop 5 Recommendations for someone who liked '{seed_movie}':")
    recs = get_recommendations(seed_movie, df, cosine_sim, n=5)
    if isinstance(recs, pd.DataFrame):
        print(recs.to_string(index=False))
    else:
        print(recs)
        
    seed_movie_2 = "Casino"
    print(f"\nTop 5 Recommendations for someone who liked '{seed_movie_2}':")
    recs2 = get_recommendations(seed_movie_2, df, cosine_sim, n=5)
    if isinstance(recs2, pd.DataFrame):
        print(recs2.to_string(index=False))
    else:
        print(recs2)
    
    print("\nPipeline Complete!")

if __name__ == "__main__":
    main()
