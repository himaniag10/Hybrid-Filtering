# Technologies Used

This project was built utilizing modern data science and NLP tools.

### Core Languages & Libraries
* **Python 3.9+**: The core programming language.
* **Pandas**: Used in `data_loader.py` for highly efficient DataFrame manipulation and NaN handling.
* **Scikit-Learn**: The powerhouse behind our NLP engine.
  * `TfidfVectorizer`: Used to convert raw text (Plots, Actors, Genres) into a matrix of TF-IDF features.
  * `cosine_similarity`: Used to calculate the mathematical distance/similarity between vectorized movies.

### API & Data Fetching
* **Requests**: Used to query the RESTful OMDb API.
* **python-dotenv**: Used for secure management of API credentials.

### Interactive Development
* **Jupyter / IPython**: Used for initial exploratory data analysis and algorithm prototyping.
