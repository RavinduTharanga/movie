# from data_loader import load_movies
# from vector_store import VectorStore

# # Load data
# df = load_movies()
# vector_store = VectorStore(df['combined'].tolist())

# def get_recommendations(query):
#     idxs = vector_store.search(query)
#     results = df.iloc[idxs]
#     return results[['title', 'overview']].to_dict(orient='records')


from data_loader import load_movies
from vector_store import VectorStore

df = load_movies()
vector_store = VectorStore(movie_texts=None)  # Load saved model by default

def get_recommendations(query):
    idxs = vector_store.search(query)
    results = df.iloc[idxs]
    return results[['title', 'overview']].to_dict(orient='records')

