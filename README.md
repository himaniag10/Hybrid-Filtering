# 🎬 WatchWise — Intelligent NLP Movie Recommender

WatchWise is a production-grade **Machine Learning** application that uses **Natural Language Processing (NLP)** to provide hyper-relevant movie recommendations based on textual metadata like Plot, Genres, Directors, and Actors. 

Unlike basic Collaborative Filtering systems that require millions of user ratings, this system can recommend brand new movies instantly simply by reading their plot summaries.

---

## 📚 Documentation Index

We have fully documented every aspect of this project to make it easy for developers to explore, run, and contribute. Please follow the guides below:

1. 📥 [Cloning the Repository](docs/CLONING.md)
2. ⚙️ [Environment & API Setup](docs/ENVIRONMENT.md)
3. 🚀 [Getting Started & Running the Code](docs/GETTING_STARTED.md)
4. 🗂️ [Folder Structure & Architecture](docs/STRUCTURE.md)
5. 🛠️ [Technologies & Algorithms Used](docs/TECHNOLOGIES.md)
6. 🤝 [How to Contribute](docs/CONTRIBUTING.md)

---

## 🧠 How It Works (At a Glance)

1. **Data Enrichment**: We query the OMDb API to fetch massive amounts of metadata for thousands of movies (including IMDB Ratings, Posters, and detailed Plot summaries).
2. **Text Processing**: In `src/data_loader.py`, we intelligently handle missing values and merge all text fields (`Plot`, `Genre`, `Director`, `Actors`) into a massive `content` string.
3. **TF-IDF Vectorization**: We use Scikit-Learn to convert these text strings into vectors, stripping out stop words and assigning weights to important keywords (e.g., "Mafia", "Space").
4. **Cosine Similarity**: We calculate the mathematical angle between every movie vector. If two movies have similar plots and directors, their cosine similarity score approaches `1.0`.
5. **Inference**: You provide a seed movie (e.g., *"Casino"*), and the system instantly returns the top 5 closest vectors (e.g., *"Goodfellas"*, *"Taxi Driver"*).

---
*Designed with production-grade architecture, isolated environments, and dynamic path management.*
