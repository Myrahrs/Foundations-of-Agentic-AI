import streamlit as st
import os
import requests
import tempfile
from io import StringIO
from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from transformers import pipeline
from langchain.llms import HuggingFacePipeline

# Set Hugging Face API key from Streamlit secrets
os.environ["HUGGINGFACEHUB_API_TOKEN"] = st.secrets["HUGGINGFACE_API_TOKEN"]

# Streamlit page setup
st.set_page_config(page_title="Canvas QA Assistant", layout="centered")

st.title("📘 Hi, I'm AskEd - Ask Me About our Canvas LMS or AI Classes")
st.write("Please ask questions!")

@st.cache_resource
def load_qa_chain():
    # ✅ Load your Canvas documentation from GitHub
    url = "https://raw.githubusercontent.com/Myrahrs/Foundations-of-Agentic-AI/AAIDC-Module-1-Project/data/canvas_docs.txt"
    response = requests.get(url)
    response.raise_for_status()

    # ✅ Save content to a temporary file
    with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".txt") as tmp_file:
        tmp_file.write(response.text)
        tmp_file_path = tmp_file.name

    # ✅ Load documents from the temp file
    loader = TextLoader(tmp_file_path)
    documents = loader.load()

    # ✅ Create embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # ✅ Build vector store and retriever
    vector_store = FAISS.from_documents(documents, embeddings)
    retriever = vector_store.as_retriever()

    # ✅ Setup Hugging Face text generation pipeline
    hf_pipe = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        device=-1  # Use CPU
    )

    llm = HuggingFacePipeline(
        pipeline=hf_pipe,
        model_kwargs={"max_length": 256, "temperature": 0.5}
    )

    # ✅ Return QA chain
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Load the QA chain (cached)
qa_chain = load_qa_chain()

# User input and interaction
query = st.text_input("🔎 Enter your question about Canvas LMS:")

if st.button("Get Answer") and query.strip():
    with st.spinner("Thinking..."):
        try:
            response = qa_chain.run(query)
            st.success("✅ Answer:")
            st.write(response)
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
