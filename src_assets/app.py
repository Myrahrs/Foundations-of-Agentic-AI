import streamlit as st
import os
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
    # Load your Canvas documentation from a txt file
    loader = TextLoader("data/canvas_docs.txt")
    documents = loader.load()

    # Create embeddings with sentence-transformers model
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create FAISS vector store from documents and embeddings
    vector_store = FAISS.from_documents(documents, embeddings)
    retriever = vector_store.as_retriever()

    # Create a Hugging Face pipeline for text2text-generation using flan-t5-base
    hf_pipe = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        device=-1  # Use CPU; change to device=0 if GPU available
    )

    # Wrap the HF pipeline in LangChain LLM interface, pass generation params here
    llm = HuggingFacePipeline(
        pipeline=hf_pipe,
        model_kwargs={"max_length": 256, "temperature": 0.5}
    )

    # Build RetrievalQA chain using the retriever and LLM
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
