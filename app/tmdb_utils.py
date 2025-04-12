# app/tmdb_utils.py

import requests

API_KEY = "YOUR_TMDB_API_KEY"  # <-- Put your real key here

def get_movie_poster(title):
    url = f"https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": API_KEY,
        "query": title
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if data["results"]:
        poster_path = data["results"][0].get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return None
