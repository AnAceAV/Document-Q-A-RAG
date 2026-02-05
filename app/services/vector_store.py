import faiss
import os
from utils.config import FAISS_PATH

class VectorStore:
    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)

    def add(self, embeddings):
        self.index.add(embeddings)

    def save(self):
        os.makedirs(FAISS_PATH, exist_ok=True)
        faiss.write_index(self.index, f"{FAISS_PATH}/index.faiss")

    def load(self):
        self.index = faiss.read_index(f"{FAISS_PATH}/index.faiss")
