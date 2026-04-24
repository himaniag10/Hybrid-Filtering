import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from pathlib import Path
from .config import BASE_DIR

def run_kmeans_and_plot(tfidf_matrix, max_k=10):
    """
    Runs K-Means multiple times to find the optimal 'K' and saves the Elbow plot.
    """
    inertia = []
    k_range = range(1, max_k + 1)
    
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(tfidf_matrix)
        inertia.append(kmeans.inertia_)
    
    # Plotting the Elbow Curve
    plt.figure(figsize=(10, 6))
    plt.plot(k_range, inertia, 'bx-')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Inertia (Error)')
    plt.title('The Elbow Method for Optimal K')
    
    output_path = BASE_DIR / "Outputs" / "elbow_curve.png"
    plt.savefig(output_path)
    plt.close()
    
    # Fit the "optimal" model (let's assume 8 for now or pick based on data)
    optimal_k = 8
    model = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
    clusters = model.fit_predict(tfidf_matrix)
    
    return clusters, output_path

def train_model(df, tfidf_matrix):
    """
    Wrapper for training the unsupervised model.
    """
    clusters, plot_path = run_kmeans_and_plot(tfidf_matrix)
    df['cluster'] = clusters
    return df, plot_path
