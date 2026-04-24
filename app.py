import streamlit as st
import pandas as pd
from src.data_loader import load_and_clean_data
from src.features import engineer_features
from src.recommend import get_recommendations
from pathlib import Path

# Page Config
st.set_page_config(page_title="AI Movie Recommender", page_icon="🎬", layout="wide")

# Caching Data & Model
@st.cache_resource
def init_pipeline():
    df = load_and_clean_data()
    cosine_sim = engineer_features(df)
    return df, cosine_sim

df, cosine_sim = init_pipeline()

# UI Layout
st.title("🎬 NLP-Powered Movie Recommender")
st.markdown("""
    This recommendation engine uses **Natural Language Processing (TF-IDF)** and **Machine Learning** 
    to suggest movies based on their plot summaries, genres, and cast.
""")

# Sidebar
st.sidebar.header("Settings")
n_recs = st.sidebar.slider("Number of Recommendations", 1, 10, 5)

# Main Interaction
tab1, tab2 = st.tabs(["Recommendations", "Model Analytics"])

with tab1:
    movie_list = df['title'].values
    selected_movie = st.selectbox("Type or select a movie you like:", movie_list)

    if st.button("Get Recommendations"):
        with st.spinner("Analyzing movie plots..."):
            recs = get_recommendations(selected_movie, df, cosine_sim, n=n_recs)
            
            if isinstance(recs, str):
                st.error(recs)
            else:
                st.subheader(f"Because you liked '{selected_movie}':")
                
                # Display results in columns
                cols = st.columns(min(n_recs, 5))
                
                # Check for Poster data
                # Assuming get_recommendations returns title, imdbRating, sim_score, reason, Plot, Poster
                # Let's verify the columns returned by get_recommendations in src/recommend.py
                
                for i, row in recs.iterrows():
                    with cols[i % 5]:
                        # Poster fallback
                        poster_url = row.get('Poster', 'https://via.placeholder.com/300x450?text=No+Poster')
                        if pd.isna(poster_url) or poster_url == 'N/A':
                            poster_url = 'https://via.placeholder.com/300x450?text=No+Poster'
                        
                        st.image(poster_url, use_column_width=True)
                        st.markdown(f"**{row['title']}**")
                        st.write(f"⭐ IMDB: {row['imdbRating']}")
                        st.write(f"🎯 Match: {int(row['sim_score'] * 100)}%")
                        
                        with st.expander("See Plot"):
                            st.write(row.get('Plot', 'No plot summary available.'))

with tab2:
    st.header("📊 Machine Learning Performance")
    st.write("Below is the **Elbow Method** graph used to determine the optimal number of clusters for our movie database.")
    
    elbow_plot_path = Path(__file__).resolve().parent / "Outputs" / "elbow_curve.png"
    if elbow_plot_path.exists():
        st.image(str(elbow_plot_path), caption="Elbow Curve (Unsupervised Learning Evaluation)")
        st.markdown("""
            **What does this mean?**
            The 'Elbow' point on this graph helps us identify the most efficient way to group our 1,000+ movies. 
            By using this scientific method instead of guessing, our AI creates much more distinct and accurate movie categories.
        """)
    else:
        st.warning("Elbow curve plot not found. Run 'python src/main.py' to generate it.")
