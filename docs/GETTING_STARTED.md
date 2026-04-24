# Getting Started

Once you have cloned the repository and set up your environment, you are ready to run the recommender!

### 1. Generating Enriched Data (Optional)
If you want to fetch new movies from the OMDb API:
```bash
python3 generating_data/generating.py
```
This will append new movies with full Plot, Director, and Actor metadata to `Dataset/enriched_movies.csv`.

### 2. Running the Recommendation Pipeline
To execute the NLP Content-Based Recommender, simply run the main orchestrator:
```bash
python3 src/main.py
```

### What happens when you run `main.py`?
1. The script loads the enriched dataset.
2. It concatenates the Plot, Genre, Director, and Actors into a single text document per movie.
3. It passes this text through a **TF-IDF Vectorizer** to extract the mathematical importance of each word.
4. It calculates the **Cosine Similarity** between every movie.
5. It outputs the top 5 most similar movies to a given seed movie.
