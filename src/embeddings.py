from sentence_transformers import SentenceTransformer

def get_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(texts):
    model = get_model()
    return model.encode(texts)