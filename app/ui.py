import streamlit as st
from llm_recommender import get_recommendations

st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")
st.title("🎬 Free Movie Recommender (LLM + TMDB)")

user_input = st.text_input("Describe the kind of movie you want to watch:")

if st.button("Recommend"):
    if not user_input.strip():
        st.warning("Please enter a movie description.")
    else:
        with st.spinner("Finding movies..."):
            recommendations = get_recommendations(user_input)
            for movie in recommendations:
                st.subheader(movie['title'])
                st.write(movie['overview'])
