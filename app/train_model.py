# train_model.py
from data_loader import load_movies
from vector_store import VectorStore

print("📥 Loading dataset...")
df = load_movies()
texts = df['combined'].tolist()

print("🔧 Building vector store and computing embeddings...")
vector_store = VectorStore(movie_texts=texts)

print("💾 Saving model to disk...")
vector_store.save("embeddings.pkl", "index.pkl")
print("✅ Done! Model saved as 'embeddings.pkl' and 'index.pkl'.")
