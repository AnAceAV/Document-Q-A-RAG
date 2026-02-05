import numpy as np

def retrieve(query_embedding, vector_store, top_k=3):
    distances, indices = vector_store.index.search(
        np.array([query_embedding]), top_k
    )
    return indices[0]
