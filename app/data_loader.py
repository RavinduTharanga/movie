# import pandas as pd

# def load_movies(path="https://drive.google.com/drive/u/0/home"):
#     df = pd.read_csv(path)
#     df = df[['title', 'overview', 'genres']].dropna()
#     df['combined'] = df['title'] + " - " + df['overview'] + " Genres: " + df['genres']
#     return df


# from kagglehub import KaggleDatasetAdapter
# import kagglehub
# import pandas as pd

# def load_movies():
#     file_path = kagglehub.load_dataset(
#         KaggleDatasetAdapter.PANDAS,
#         "asaniczka/tmdb-movies-dataset-2023-930k-movies",
#         "TMDB_movie_dataset_v11.csv"
#     )
    
#     df = pd.read_csv(file_path)
#     df = df[['title', 'overview', 'genres']].dropna()
#     df['combined'] = df['title'] + " - " + df['overview'] + " Genres: " + df['genres']
#     return df


import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter

def load_movies():
    # Load directly as DataFrame, not file path
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "asaniczka/tmdb-movies-dataset-2023-930k-movies",
        "TMDB_movie_dataset_v11.csv"
    )
    df = df[['title', 'overview', 'genres']].dropna()
    df['combined'] = df['title'] + " - " + df['overview'] + " Genres: " + df['genres']
    return df

