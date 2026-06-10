# 🎬 Movie Recommendation System

## 📌 Overview

The Movie Recommendation System is a Machine Learning-based web application that recommends movies similar to a user's selected movie. The system uses Content-Based Filtering techniques to analyze movie metadata and generate personalized recommendations.

Built with Python, Scikit-Learn, and Streamlit, this project demonstrates the practical application of recommendation systems used by modern streaming platforms.

---

## 🚀 Features

* Recommend movies based on similarity
* Interactive Streamlit web interface
* Content-Based Filtering approach
* Fast recommendation generation using Cosine Similarity
* Clean and user-friendly design
* Real-time movie selection and recommendations

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Pickle

---

## 📊 Dataset

Dataset Used:

* TMDB 5000 Movies Dataset
* TMDB 5000 Credits Dataset

The dataset contains movie information such as:

* Movie Title
* Overview
* Genres
* Keywords
* Cast
* Crew

---

## ⚙️ Machine Learning Workflow

### 1. Data Collection

Loaded movie and credits datasets.

### 2. Data Preprocessing

* Merged datasets
* Removed missing values
* Extracted genres, cast, crew, and keywords
* Created combined tags for each movie

### 3. Feature Engineering

Generated movie feature vectors using:

* CountVectorizer
* Maximum Features: 5000
* English Stop Words Removal

### 4. Similarity Calculation

Calculated similarity scores using:

* Cosine Similarity

### 5. Recommendation Generation

Returned the Top 5 most similar movies based on similarity scores.

---

## 📂 Project Structure

movie-recommender-system/

├── app.py

├── requirements.txt

├── README.md

├── test.py

├── model/

│   ├── movies.pkl

│   └── similarity.pkl

├── src/

│   ├── recommender.py

│   └── model.py

├── tmdb_5000_movies.csv

└── tmdb_5000_credits.csv

---

## ▶️ How to Run

### Clone Repository

git clone YOUR_GITHUB_REPOSITORY_URL

cd movie-recommender-system

### Create Virtual Environment

python -m venv venv

source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

### Generate Model Files

python src/recommender.py

### Run Application

streamlit run app.py

---

## 📸 Sample Output

Selected Movie:

Avatar

Recommended Movies:

* Titan A.E.
* Small Soldiers
* Independence Day
* Ender's Game
* Aliens vs Predator: Requiem

---

## 🔮 Future Enhancements

* Movie Poster Integration using TMDB API
* IMDb Ratings Display
* Multilingual Movie Recommendations
* Genre-Based Filtering
* User Authentication
* Hybrid Recommendation System

---

## 👩‍💻 Developer

**Sakkari Jhansi Rani**

AI Intern | Web Developer | Machine Learning Enthusiast

---

## ⭐ If you found this project useful, consider giving it a star on GitHub.
