import pandas as pd

def get_recommendations(title, df, cosine_sim, n=5):
    # Find index of movie
    idx = df.index[df['title'] == title].tolist()
    if not idx:
        idx = df.index[df['clean_title'] == title].tolist()
    
    if not idx:
        return f"Movie '{title}' not found in the dataset."
        
    idx = idx[0]
    
    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n+1]
    
    movie_indices = [i[0] for i in sim_scores]
    scores = [i[1] for i in sim_scores]
    
    results = df.iloc[movie_indices].copy()
    results['sim_score'] = scores
    results['reason'] = f"Similar Plot/Genre to {title}"
    
    return results[['title', 'imdbRating', 'sim_score', 'reason']]
