import pandas as pd
import requests
import time
import os
import re

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OMDB_API_KEY")
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_FILE = BASE_DIR / "Dataset" / "enriched_movies.csv"
MOVIES_PATH = BASE_DIR / "Dataset" / "Raw" / "movies.csv"

# Load dataset
movies = pd.read_csv(MOVIES_PATH)

# Clean title
def clean_title(title):
    return re.sub(r"\(\d{4}\)", "", title).strip()

movies["clean_title"] = movies["title"].apply(clean_title)

# Load existing CSV
if os.path.exists(OUTPUT_FILE):
    existing_df = pd.read_csv(OUTPUT_FILE)
    existing_titles = set(existing_df["title"].str.lower())
else:
    existing_df = pd.DataFrame()
    existing_titles = set()

print(f"Already have {len(existing_titles)} movies")

# Fetch OMDb data
def fetch_movie(title):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={title}"
    
    try:
        res = requests.get(url)
        data = res.json()
        
        if data.get("Response") == "True":
            return data
    except Exception as e:
        print("Error:", e)
    
    return {}

# MAIN LOOP
new_rows = []
count = 0
LIMIT = 1000

for _, row in movies.iterrows():
    if count >= LIMIT:
        break

    title = row["clean_title"]

    # Skip already stored
    if title.lower() in existing_titles:
        continue

    print(f"Fetching: {title}")

    omdb_data = fetch_movie(title)

    # Merge original row + OMDb data
    combined = row.to_dict()
    combined.update(omdb_data)

    new_rows.append(combined)
    existing_titles.add(title.lower())
    count += 1

    time.sleep(0.2)

print(f"Fetched {count} new movies")

# Save
if new_rows:
    new_df = pd.DataFrame(new_rows)

    if existing_df.empty:
        new_df.to_csv(OUTPUT_FILE, index=False)
    else:
        new_df.to_csv(OUTPUT_FILE, mode='a', header=False, index=False)

    print("✅ Data appended with ALL columns")
else:
    print("No new data found")