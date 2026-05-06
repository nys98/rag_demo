import faiss
import numpy as np

def build_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index


def search(index, query_vector, k=3):
    D, I = index.search(query_vector, k)
    return I