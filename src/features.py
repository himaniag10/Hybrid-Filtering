from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def engineer_features(df):
    tfidf = TfidfVectorizer(stop_words='english')
    # Use the combined 'content' string to create features
    tfidf_matrix = tfidf.fit_transform(df['content'])
    
    # Compute cosine similarity between all movies based on text features
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    return cosine_sim
