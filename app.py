# app.py - Stockdale Canvas QA Streamlit App

import streamlit as st
import os
from langchain.chains import RetrievalQA
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from langchain_community.document_loaders import TextLoader

# Set your API key from Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Set page config
st.set_page_config(page_title="Canvas QA Assistant", layout="centered")

st.title("📘 Ask Me About Canvas LMS")
st.write("Upload documentation and ask questions!")

# Load documents (if not already embedded)
@st.cache_resource
def load_qa_chain():
    loader = TextLoader("canvas_docs.txt")
    documents = loader.load()

    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(documents, embeddings)

    retriever = vector_store.as_retriever()
    llm = OpenAI()
    return RetrievalQA(llm=llm, retriever=retriever)

qa_chain = load_qa_chain()

# User input
query = st.text_input("🔎 Enter your question about Canvas LMS:")
if st.button("Get Answer") and query.strip():
    with st.spinner("Thinking..."):
        try:
            response = qa_chain.run(query)
            st.success("✅ Answer:")
            st.write(response)
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
