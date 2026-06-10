import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")

# Merge datasets (basic version)
movies = movies.merge(credits, on="title")

# Create a simple content feature
movies = movies[['id', 'title', 'overview']]
movies['overview'] = movies['overview'].fillna('')

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['overview']).toarray()

# Similarity matrix
similarity = cosine_similarity(vectors)

# Save model files
import os
os.makedirs("model", exist_ok=True)

pickle.dump(movies, open("model/movies.pkl", "wb"))
pickle.dump(similarity, open("model/similarity.pkl", "wb"))

print("✅ Model trained and saved successfully!")
