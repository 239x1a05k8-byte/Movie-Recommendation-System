import streamlit as st
import pickle

from src.model import recommend

# Page Configuration
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background: linear-gradient(to right, #141E30, #243B55);
}

.main-title{
    text-align:center;
    color:white;
    font-size:55px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:#d3d3d3;
    font-size:22px;
    margin-bottom:30px;
}

.card{
    background-color:#1f2937;
    padding:20px;
    border-radius:15px;
    text-align:center;
    color:white;
    font-size:18px;
    font-weight:bold;
    box-shadow:0px 4px 10px rgba(0,0,0,0.4);
}

.footer{
    text-align:center;
    color:white;
    margin-top:50px;
    font-size:16px;
}

.stButton>button{
    width:100%;
    background-color:#ff4b4b;
    color:white;
    border-radius:10px;
    height:50px;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("👩‍💻 Developer")

st.sidebar.success("Sakkari Jhansi Rani")

st.sidebar.markdown("---")

st.sidebar.header("📌 Project Info")

st.sidebar.write("""
This project recommends movies using:

✅ Content-Based Filtering

✅ Count Vectorization

✅ Cosine Similarity

✅ Streamlit

Dataset Used:
TMDB 5000 Movies Dataset
""")

# Load Model
movies = pickle.load(open('model/movies.pkl', 'rb'))

# Header
st.markdown(
    '<div class="main-title">🎬 Movie Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Find Movies Similar To Your Favorites Instantly</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# Movie Selection
selected_movie = st.selectbox(
    "🎥 Select a Movie",
    movies['title'].values
)

# Recommend Button
if st.button("🚀 Get Recommendations"):

    recommendations = recommend(selected_movie)

    st.markdown("## ✨ Recommended Movies")

    col1, col2, col3, col4, col5 = st.columns(5)

    cards = [col1, col2, col3, col4, col5]

    for i in range(len(recommendations)):
        with cards[i]:
            st.markdown(
                f"""
                <div class="card">
                🎬<br><br>
                {recommendations[i]}
                </div>
                """,
                unsafe_allow_html=True
            )

st.markdown("---")

st.markdown(
    """
    <div class="footer">
    Developed with by <b>Sakkari Jhansi Rani</b><br>
    AI Intern | Web Developer | CSE Student
    </div>
    """,
    unsafe_allow_html=True
)
