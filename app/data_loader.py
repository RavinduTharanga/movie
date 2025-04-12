# import pandas as pd

# def load_movies(path="TMDB.csv"):
#     df = pd.read_csv(path)
#     df = df[['title', 'overview', 'genres']].dropna()
#     df['combined'] = df['title'] + " - " + df['overview'] + " Genres: " + df['genres']
#     return df


import pandas as pd

# Optional: pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Load the dataset file from KaggleHub
file_path = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "asaniczka/tmdb-movies-dataset-2023-930k-movies",
    "TMDB_movie_dataset_v11.csv"  # Make sure this file exists in the dataset
)

# Define function to process the movie dataset
def load_movies(file_path):
    df = pd.read_csv(file_path)
    df = df[['title', 'overview', 'genres']].dropna()
    df['combined'] = df['title'] + " - " + df['overview'] + " Genres: " + df['genres']
    return df

# Load and process the dataset
movies_df = load_movies(file_path)
print("First 5 records:")
print(movies_df.head())

