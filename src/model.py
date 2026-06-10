import pickle
import os
import numpy as np

# Get current directory of this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go one level up to project root
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# Correct paths
movies_path = os.path.join(PROJECT_ROOT, "model", "movies.pkl")
similarity_path = os.path.join(PROJECT_ROOT, "model", "similarity.pkl")

# Load files safely
movies = pickle.load(open(movies_path, "rb"))
similarity = pickle.load(open(similarity_path, "rb"))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    for i in movie_list:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations
