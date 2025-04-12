from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorStore:
    def __init__(self, movie_texts):
        self.model = SentenceTransformer("all-MiniLM-L6-v2", device='cuda')
        self.movie_texts = movie_texts
        self.embeddings = self.model.encode(movie_texts, show_progress_bar=True)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings))

    def search(self, query, top_k=5):
        query_vec = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_vec), top_k)
        return indices[0]
