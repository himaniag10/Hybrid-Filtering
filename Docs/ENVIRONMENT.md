# Environment Setup

This project uses `python-dotenv` to manage secrets and API keys safely.

### 1. Creating the Virtual Environment
It is highly recommended to use a virtual environment to isolate the project's dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 2. Installing Dependencies
With your virtual environment active, install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Setting Up the `.env` File
This project fetches real-time movie data using the OMDb API. You need a free API key to fetch new data.
1. Get a free API key from [OMDb API](http://www.omdbapi.com/).
2. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
3. Open `.env` and replace `your_api_key_here` with your actual key:
   ```env
   OMDB_API_KEY=16d979c3
   ```
