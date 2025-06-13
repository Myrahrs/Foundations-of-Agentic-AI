# app.py - Stockdale Canvas QA Streamlit App (Hugging Face version)

import streamlit as st
import os
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFaceHub  # or Ollama if running locally

# --- STREAMLIT CONFIG ---
st.set_page_config(page_title="Canvas QA Assistant", layout="centered")
st.title("📘 Ask Me About Canvas LMS")
st.write("Upload documentation and ask questions!")

# --- EMBEDDINGS SETUP ---
@st.cache_resource
def load_qa_chain():
    loader = TextLoader("canvas_docs.txt", encoding='utf-8')
    documents = loader.load()

    # Use Hugging Face MiniLM embeddings (small + fast)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vector_store = FAISS.from_documents(documents, embeddings)
    retriever = vector_store.as_retriever()

    # Hugging Face LLM (e.g., google/flan-t5-small or openassistant)
    llm = HuggingFaceHub(
        repo_id="google/flan-t5-base",  # or "tiiuae/falcon-7b-instruct" (requires Hugging Face API key)
        model_kwargs={"temperature": 0.7, "max_length": 512},
        huggingfacehub_api_token=st.secrets["HF_API_KEY"]  # You’ll need to add this to Streamlit secrets
    )

    return RetrievalQA(llm=llm, retriever=retriever)

qa_chain = load_qa_chain()

# --- USER INPUT ---
query = st.text_input("🔎 Enter your question about Canvas LMS:")
if st.button("Get Answer") and query.strip():
    with st.spinner("Thinking..."):
        try:
            response = qa_chain.run(query)
            st.success("✅ Answer:")
            st.write(response)
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")