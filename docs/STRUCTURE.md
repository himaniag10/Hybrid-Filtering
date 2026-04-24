# Project Structure

This repository is built following senior-level software engineering standards, fully modularizing the Machine Learning logic.

```text
├── Dataset/
│   └── enriched_movies.csv   # The NLP dataset containing plots and metadata
├── docs/                         # All project documentation
├── generating_data/
│   └── generating.py             # Script to fetch live OMDb API data
├── Notebooks/
│   └── Recommendation_Walkthrough.ipynb # Beginner-friendly tutorial
├── src/                          # Main source code directory
│   ├── config.py                 # Centralized pathlib configuration
│   ├── data_loader.py            # Handles Pandas data loading and NaN cleaning
│   ├── features.py               # Houses the TF-IDF Vectorization & Cosine Sim
│   ├── models.py                 # K-Means clustering & Elbow plotting
│   ├── recommend.py              # The core inference logic for matching movies
│   └── main.py                   # The entry point that orchestrates the modules
├── app.py                        # Streamlit Interactive UI
├── .env.example                  # Template for environment variables
├── requirements.txt              # Python dependencies
└── README.md                     # Main project overview
```
