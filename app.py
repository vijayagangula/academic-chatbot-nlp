import streamlit as st
from chatbot_engine import get_answer, setup_index

# Build index when app starts
setup_index()

st.set_page_config(page_title="Academic Chatbot", page_icon="🎓")
st.title("🎓 Academic Query Chatbot")
st.markdown("Ask any academic-related question below:")

query = st.text_input("📘 Your Question")

if st.button("Get Answer"):
    if query.strip() == "":
        st.warning("Please enter a question.")
    else:
        response = get_answer(query)
        st.success(f"📢 Answer: {response}")
