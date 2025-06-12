
# 📘 Canvas LMS Chatbot – Project 1: Foundations of Agentic AI

## Project Description

This project is a solo exploration into building a chatbot powered by Agentic AI that can answer questions based on uploaded Canvas LMS documentation. The chatbot utilizes document embeddings, retrieval-based QA, and a Streamlit interface to deliver intelligent, context-aware responses to user queries.

---

## My Project Idea

I built a **Canvas LMS Q&A assistant** that allows users to upload official documentation (e.g., `.txt` or `.pdf` files exported from Canvas help guides) and ask natural language questions. The chatbot retrieves relevant passages using embeddings and FAISS-based vector search, then generates concise answers using a language model.

---

## Plan & Approach

As a solo developer, I approached the project in manageable phases:

1. **Define** the scope: Q&A from Canvas documentation.
2. **Prepare** the documents (text format) for ingestion.
3. **Build** the Streamlit interface for uploading files and submitting questions.
4. **Load** and embed documents using LangChain and OpenAI embeddings.
5. **Create** a retrieval-augmented QA chain using FAISS.
6. **Test** functionality while minimizing API token usage.

---

## Development Tools & Learning Resources

- **LangChain** for building the embedding and retrieval pipelines
- **OpenAI API** for embedding and LLM responses
- **FAISS** for vector storage and similarity search
- **Streamlit** for the web-based interface
- Help from lectures, LangChain documentation, and AI community guides

To manage cost and quota limits during testing, I:
- Cached embeddings locally
- Mocked responses during interface debugging
- Limited input sizes and test queries

---

## How to Run the App

1. Clone the repository  
   git clone https://github.com/yourusername/myrahrs_Foundations_of_Agentic_AI.git
   cd "myrahrs_Foundations_of_Agentic_AI/Project 1"

## Thorough Documentation for Grading, Troubleshooting, etc.

Canvas LMS Chatbot Assistant

Overview

This project is an AI-powered chatbot that allows users to upload Canvas LMS documents (e.g., syllabi, schedules, policies) and ask natural language questions about the content. The chatbot uses Retrieval-Augmented Generation (RAG) to generate responses grounded in the uploaded documents.

It’s built using LangChain, OpenAI embeddings, FAISS, and Streamlit for a user-friendly web interface.

---

Project Objectives

- Provide students with an intuitive way to access course documents using natural language.
- Apply retrieval-augmented generation (RAG) techniques to education-specific use cases.
- Develop a reproducible framework for building course-specific chatbots using LangChain and OpenAI.

---

Features

- Upload one or more Canvas LMS documents (PDF or .txt).
- Ask free-form questions like “What’s the attendance policy?” or “When is the final project due?”
- Retrieves context-relevant answers from the uploaded materials using FAISS vector search.
- Interface hosted with Streamlit for ease of use.

---

Installation Instructions

1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/canvas-lms-chatbot.git
cd canvas-lms-chatbot/Project\ 1

2. Set Up a Virtual Environment

python -m venv venv
.
env\Scripts ctivate     # On Windows

3. Install Required Packages

pip install -r requirements.txt

If you encounter errors with missing packages, run:

pip install tiktoken langchain-openai

4. Run the App

streamlit run app.py

Then open your browser and go to:  
http://localhost:8502

---

Directory Structure

Foundations_of_Agentic_AI_Project_1/
├── app.py  ←  Streamlit app
├── canvas_docs.txt  ← Source file
├── .streamlit/
│   └── secrets.toml  ← API key config
└── README.md           # Full project documentation

---

How It Works

1. Uploaded files are split into chunks using LangChain's document loaders.
2. Chunks are embedded using OpenAI's embeddings and stored in a FAISS vector database.
3. When a user submits a query, relevant chunks are retrieved via semantic similarity.
4. The query and retrieved context are passed to an OpenAI language model to generate a grounded response.

---

Sample Questions

| Question Prompt                        | Expected Outcome                                                  |
|----------------------------------------|-------------------------------------------------------------------|
| What is the attendance policy?         | Returns the relevant policy from your uploaded syllabus           |
| When are the midterm exams?            | Finds exam dates in the schedule or assignment section            |
| What topics are covered in Week 3?     | Provides info from the calendar or weekly breakdown               |
| How much is participation worth?       | Extracts grading breakdown or participation policy                |

---

Troubleshooting

| Issue                                  | Resolution                                                                 |
|----------------------------------------|----------------------------------------------------------------------------|
| ModuleNotFoundError: tiktoken          | Run pip install tiktoken                                                   |
| langchain_community not found          | Run pip install langchain langchain-community                              |
| openai.RateLimitError: 429             | Check API quota at https://platform.openai.com/account                    |
| FileNotFoundError: app.py              | Ensure you're in the correct folder before running the app                 |

---

Technical Stack

| Tool         | Purpose                                    |
|--------------|--------------------------------------------|
| Python       | Core development language                  |
| Streamlit    | Web-based UI                               |
| LangChain    | Document QA and chain orchestration        |
| OpenAI API   | Embeddings and language model responses    |
| FAISS        | Vector search for document retrieval       |

---

Evaluation Against Technical Rubric

This project aligns with >70% of the Ready Tensor Technical Evaluation Rubric for tools/apps:

| Criterion                         | Status | Description                                                      |
|----------------------------------|--------|------------------------------------------------------------------|
| Well-defined purpose             | ✅     | Clear student-centered chatbot for LMS document access           |
| Comprehensive technical docs     | ✅     | Installation, usage, structure, and troubleshooting included     |
| Practical application            | ✅     | Aids in student access to syllabus and Canvas content            |
| Reproducibility                  | ✅     | All dependencies and steps fully documented                      |
| Extensibility                    | ✅     | Designed for other courses or platforms with minimal changes     |
| Automated evaluation             | ❌     | No unit tests or CI/CD pipeline included (future improvement)    |

---

Future Enhancements

- Canvas API integration for dynamic syllabus syncing
- Role-based views for students vs. instructors
- Add memory and tools support for follow-up conversation
- Improved PDF parsing and OCR for image-based documents

---

License

MIT License. You are free to use, adapt, and distribute for educational or personal use.

---

Author

Developed by Myrah Stockdale for the Foundations of Agentic AI course, Ready Tensor 2025. This project was completed independently as a solo developer submission.
