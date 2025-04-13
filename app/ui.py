# import streamlit as st
# from llm_recommender import get_recommendations

# st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")
# st.title("🎬 Free Movie Recommender (LLM + TMDB)")

# user_input = st.text_input("Describe the kind of movie you want to watch:")

# if st.button("Recommend"):
#     if not user_input.strip():
#         st.warning("Please enter a movie description.")
#     else:
#         with st.spinner("Finding movies..."):
#             recommendations = get_recommendations(user_input)
#             for movie in recommendations:
#                 st.subheader(movie['title'])
#                 st.write(movie['overview'])


import streamlit as st
from llm_recommender import get_recommendations

# Set up the Streamlit page
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender")

# Input from user
user_input = st.text_input("What kind of movie do you want to watch today?")

# Button to get recommendations
if st.button("Recommend"):
    with st.spinner("Finding the perfect movie..."):
        recommendations = get_recommendations(user_input)
        for movie in recommendations:
            st.subheader(movie['title'])
            st.write(movie['overview'])
