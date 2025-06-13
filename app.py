# app.py - Stockdale Canvas QA Streamlit App using Hugging Face

import streamlit as st
import os
from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import HuggingFaceHub

# Set Hugging Face API key
os.environ["HUGGINGFACEHUB_API_TOKEN"] = st.secrets["HUGGINGFACE_API_TOKEN"]

# Streamlit page setup
st.set_page_config(page_title="Canvas QA Assistant", layout="centered")

st.title("📘 Ask Me About Canvas LMS")
st.write("Upload documentation and ask questions!")

# Load QA chain (cached for performance)
@st.cache_resource
def load_qa_chain():
    # Load your Canvas documentation from txt
    loader = TextLoader("canvas_docs.txt")
    documents = loader.load()

    # Embeddings using sentence-transformers
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(documents, embeddings)
    retriever = vector_store.as_retriever()

    # Hugging Face LLM (flan-t5-base is free and fast)
    llm = HuggingFaceHub(
        repo_id="google/flan-t5-base",
        model_kwargs={"temperature": 0.5, "max_length": 256}
    )

    # Build QA chain
    return RetrievalQA(llm=llm, retriever=retriever)

qa_chain = load_qa_chain()

# User interaction
query = st.text_input("🔎 Enter your question about Canvas LMS:")
if st.button("Get Answer") and query.strip():
    with st.spinner("Thinking..."):
        try:
            response = qa_chain.run(query)
            st.success("✅ Answer:")
            st.write(response)
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
