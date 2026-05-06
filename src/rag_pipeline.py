import pandas as pd
from embeddings import generate_embeddings
from retrieval import build_index, search
from sentence_transformers import SentenceTransformer

def create_text(row):
    return (
        f"Generator {row['asset_id']} at {row['site']} has a health score of {row['health_score']}. "
        f"Issue: {row['issue']}. Repair history: {row['repairs']}."
    )

def run_pipeline(query):
    df = pd.read_csv("data/synthetic_generator_data.csv")
    df["text"] = df.apply(create_text, axis=1)

    embeddings = generate_embeddings(df["text"].tolist())

    index = build_index(embeddings)

    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_vec = model.encode([query])

    indices = search(index, query_vec)

    results = df.iloc[indices[0]]

    return results["text"].tolist()


if __name__ == "__main__":
    query = "Which generators have high repair issues?"
    print(run_pipeline(query))