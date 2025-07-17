from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd
import numpy as np
import pickle
import os

# Ensure folder exists
os.makedirs("vector_store", exist_ok=True)

def setup_index():
    df = pd.read_csv('data/academic_faq.csv', quotechar='"')
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(df['prompt'].tolist(), normalize_embeddings=True)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    # Save the index and dataframe
    with open("vector_store/faiss_index.pkl", "wb") as f:
        pickle.dump((index, df), f)

def get_answer(query):
    with open("vector_store/faiss_index.pkl", "rb") as f:
        index, df = pickle.load(f)

    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([query], normalize_embeddings=True)
    
    # Search for the closest match
    D, I = index.search(np.array(query_embedding), k=1)
    best_idx = I[0][0]
    best_score = D[0][0]

    # Threshold: Reject poor matches
    if best_score > 1.0:
        return "Sorry, I couldn't understand your question. Please ask something else."

    # Get the best answer
    answer = df.iloc[best_idx]['response']

    
    # In case the answer field is missing
    if pd.isna(answer):
        return "Sorry, I don't have an answer for that."

    return answer
