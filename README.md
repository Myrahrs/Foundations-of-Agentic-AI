
# 📘 Canvas LMS Chatbot – Project 1: Foundations of Agentic AI

# Canvas LMS Chatbot – Project 1: Foundations of Agentic AI

## Project Description
This solo project is an exploration into building a chatbot that uses Retrieval-Augmented Generation (RAG) to answer questions about Canvas LMS documents. Users upload documentation (e.g., syllabi, schedules), and the chatbot retrieves relevant content and generates intelligent responses using natural language processing.

## My Project Idea
I built a Q&A assistant focused on Canvas LMS, allowing users to upload help guides or course materials in .txt format and ask questions like:

- "What's the attendance policy?"
- "When is the final exam?"

The assistant uses:
- Document embeddings to understand content
- FAISS vector search to find relevant info
- Streamlit for an interactive web app

## Plan & Approach
This project was completed in phases:

1. Defined scope (Q&A on LMS documents)
2. Converted documents to .txt
3. Built a basic Streamlit interface
4. Embedded content using LangChain
5. Stored/retrieved vectors via FAISS
6. Swapped from OpenAI to Hugging Face to avoid paid API limits
7. Tested, documented, deployed

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Core development |
| Streamlit | Web interface |
| LangChain | Embedding, vector store, RAG orchestration |
| Hugging Face | Language model + embeddings (free tier) |
| FAISS | Vector similarity search |

## Features
- Upload Canvas LMS .txt documents
- Ask natural language questions
- Retrieve accurate, context-grounded responses
- Clean and simple Streamlit interface

## Requirements
- Python 3.10 or higher
- Hugging Face API Key (free account)
- Dependencies from requirements.txt

## Installation Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Myrahrs/Foundations-of-Agentic-AI.git
cd Foundations-of-Agentic-AI
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

You may also need:
```bash
pip install langchain langchain-community sentence-transformers
```

### 4. Add Your Hugging Face API Key
Create the file `.streamlit/secrets.toml` in the project root with:

```toml
HF_API_KEY = "your_huggingface_token_here"
```

You can create a token at https://huggingface.co/settings/tokens (choose Read access)

## Run the App
```bash
streamlit run app.py
```
Then open http://localhost:8501 in your browser.

## Directory Structure
```
Foundations-of-Agentic-AI/
├── app.py              # Streamlit app
├── canvas_docs.txt     # Canvas LMS content (sample)
├── requirements.txt    # Dependencies
├── .streamlit/
│   └── secrets.toml    # API credentials
└── README.md           # This file
```

## How It Works
1. Text documents are loaded and chunked via LangChain.
2. Each chunk is embedded using Hugging Face embeddings (e.g., sentence-transformers).
3. Chunks are stored in FAISS for vector similarity search.
4. On query, relevant chunks are retrieved and passed to a Hugging Face language model.
5. A grounded answer is returned via the Streamlit interface.

## Sample Questions

| Query | Response |
|-------|----------|
| What is the attendance policy? | Finds relevant section from syllabus |
| When are midterm exams? | Extracts from schedule or calendar |
| What topics are in Week 3? | Uses week breakdown to answer |
| How much is participation worth? | Grading policy from uploaded docs |

## Troubleshooting

| Issue | Fix |
|-------|-----|
| KeyError: HF_API_KEY | Make sure `.streamlit/secrets.toml` exists |
| ModuleNotFoundError: langchain_community | Run `pip install langchain langchain-community` |
| Missing model | Run `pip install sentence-transformers` |
| streamlit not found | Run `pip install streamlit` |

## Evaluation Against Technical Rubric

| Criterion | Status | Notes |
|-----------|--------|-------|
| Clear purpose | Complete | Focused on course-related chatbot Q&A |
| Complete technical docs | Complete | Installation, config, troubleshooting included |
| Real-world application | Complete | Helps students navigate Canvas course content |
| Fully reproducible | Complete | Works locally or via Streamlit Cloud |
| Extensible | Complete | Swap out models, docs, and use for other domains |
| Automated testing | Incomplete | (Future work – add unit tests or CI/CD) |

## Future Enhancements
- Canvas API integration to fetch content dynamically
- Role-based views (student vs. instructor)
- Memory and follow-up questions
- PDF & OCR support
- Local/offline RAG chatbot via Ollama

## License
Hugging Face License – Use, modify, or distribute freely for non-commercial or educational purposes.

## Author
Developed by Myrah Stockdale  
Completed as an individual submission for the Foundations of Agentic AI course – Ready Tensor, 2025
