# academic-chatbot-nlp
A Streamlit-based academic chatbot that answers student queries using NLP and semantic search with FAISS.
## Features

- Built with **Python** and **Streamlit**
- Uses **SentenceTransformer (MiniLM)** for sentence embeddings
- Fast query matching using **FAISS vector search**
- Knowledge base stored in a CSV file (`academic_faq.csv`)
- Real-time chat interface

## Project Structure

Chatbot/

├── app.py # Streamlit UI

├── chatbot_engine.py # Embedding and FAISS logic

├── requirements.txt

├── data/

│ └── academic_faq.csv # Q&A dataset

├── vector_store/

│ └── faiss_index.pkl # Auto-generated index (excluded in repo)
