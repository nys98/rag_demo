# Generator Health RAG Demo

## Overview
This project demonstrates a Retrieval‑Augmented Generation (RAG) pipeline built to simulate a real‑world generator maintenance analytics system.
The pipeline combines:

* Structured asset data
* Semantic search via embeddings
* Vector similarity retrieval
* LLM‑ready contextual responses

to enable context‑aware querying and insight generation.

## Problem Statement
Traditional analytics workflows rely on:

* SQL queries
* Dashboards
* Manual interpretation

However, answering questions like:

&nbsp; _“Why are certain generators at higher risk of failure?”_

requires combining:

* Multiple data sources
* Historical trends
* Contextual reasoning

This project demonstrates how RAG bridges that gap by augmenting AI responses with relevant business data.

## Architecture:
Synthetic Data → Text Transformation → Embeddings → Vector Index (FAISS) → Query Encoding → Similarity Search → Context Retrieval → Answer Generation

## How It Works
1. Data Generation
A synthetic dataset representing generator assets, health signals, and repair history is created to simulate real-world infrastructure analytics.

2. Text Representation
Structured data is transformed into natural language descriptions:
Generator GEN001 at New York has a health score of 0.65. 
Observed issue: oil degradation. Repair history: frequent oil-related repairs.

This enables semantic understanding during retrieval.

3. Embeddings
Each text record is converted into a vector representation using:

* sentence-transformers (MiniLM)

This allows similarity-based retrieval rather than keyword search.

4. Vector Search
FAISS (Facebook AI Similarity Search) is used to:

* index embeddings
* retrieve top‑k relevant records for a query


5. Retrieval-Augmented Querying
User query:
&nbsp; "Which generators have oil-related issues?"


┌────────────────────┐
                │  Synthetic Data    │
                │ (Generator Logs)   │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │ Text Transformation│
                │ (Structured → Text)│
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │   Embeddings       │
                │ (Sentence Model)   │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │  Vector Index      │
                │    (FAISS)         │
                └─────────┬──────────┘
                          ↑
         ┌────────────────┴──────────────┐
         │                               │
         │         User Query            │
         │  "Which generators are at risk?" 
         └───────────────┬───────────────┘
                         ↓
                ┌────────────────────┐
                │ Query Embedding    │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │ Similarity Search  │
                │  (Top-K Retrieval) │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │ Retrieved Context  │
                └─────────┬──────────┘
                          ↓
                ┌────────────────────┐
                │   RAG Response     │
                │ (LLM / Output)     │
                └────────────────────┘


Pipeline:

1. Convert query → embedding
2. Retrieve similar records
3. Inject retrieved context into response


## Example Queries

* “Which generators are at highest risk?”
* “What issues are most common across sites?”
* “Summarize repair patterns for low-health generators”
* “Explain why a generator might fail”


## Project Structure
rag-generator-demo/
│
├── data/
│   └── synthetic_generator_data.csv      # dataset used for RAG
│
├── notebooks/
│   └── rag_demo.ipynb                    # interactive demo walkthrough
│
├── src/
│   ├── data_generation.py                # synthetic data creation
│   ├── embeddings.py                    # embedding generation
│   ├── retrieval.py                     # vector search logic (FAISS)
│   └── rag_pipeline.py                  # end-to-end pipeline
│
├── README.md
└── requirements.txt

## Technologies Used

* Python
* Pandas / NumPy
* FAISS (vector search)
* Sentence Transformers (embeddings)
* (Optional) OpenAI / LLM integration

## How to Run
1. Clone the repo
&nbsp; git clone https://github.com/your-username/rag-generator-demo.git
&nbsp; cd rag-generator-demo

2. Install dependencies
&nbsp; pip install -r requirements.txt

3. Generate data
&nbsp; python src/data_generation.py

4. Run the pipeline
&nbsp; python src/rag_pipeline.py

&nbsp; Or open:
notebooks/rag_demo.ipynb

## Why This Project Matters
This project demonstrates:
* End-to-end RAG system design
* Integration of structured + unstructured data
* Real-world maintenance analytics use case
* Understanding of vector databases and semantic retrieval
* Ability to translate data into actionable insights

## Limitations & Future Improvements

* Replace FAISS with a production vector database (e.g., Databricks Vector Search)
* Add time-series features (e.g., generator run-time)
* Incorporate LLM response generation layer
* Introduce classification / risk scoring models
* Handle larger datasets with chunking strategies


## Key Takeaway

This project shows how RAG transforms raw data into intelligent, context-aware insights — enabling more intuitive, explainable analytics workflows beyond traditional SQL queries.


👤 Author
Yusong Ng
Data Scientist | Analytics | GenAI Applications

If you found this helpful
Feel free to:

⭐ Star the repo
🍴 Fork and extend it
💬 Reach out for collaboration