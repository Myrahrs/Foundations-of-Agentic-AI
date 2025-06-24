# 📘 Canvas LMS Chatbot – Project 1: Foundations of Agentic AI

A Retrieval‑Augmented Generation (RAG) assistant that answers questions about Canvas LMS course documents supplied by the user.

---

## Overview
The app lets instructors or students upload Canvas‑related text files (syllabi, schedules, policies, etc.).  Each file is chunked, embedded, stored in a FAISS vector index, and retrieved on demand via LangChain’s `RetrievalQA` chain backed by a Flan‑T5 language model served from Hugging Face.  The result is a lightweight, fully local chatbot that returns concise, context‑grounded answers through a Streamlit web UI.

## Target Audience
* **Students** – quickly locate grading policies, due dates, and lecture topics.
* **Instructors / Course Designers** – provide self‑service answers for common questions and check the clarity of course docs.
* **Educational Technologists & Researchers** – reference implementation of a small‑footprint RAG pipeline.

## Prerequisites
| Requirement | Minimum Version | Notes |
|-------------|-----------------|-------|
| Python | 3.10 | Tested on 3.10 & 3.11 |
| OS | Windows, macOS, Linux | CPU‑only by default (GPU optional) |
| Hugging Face account | Free tier | Needed to generate an API token |

Basic familiarity with the command line and virtual environments is assumed.


## Installation
```bash
# 1. Clone the repository
$ git clone https://github.com/Myrahrs/Foundations-of-Agentic-AI.git
$ cd Foundations-of-Agentic-AI

# 2. Create & activate a virtual environment
$ python -m venv venv
$ source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
(venv) $ pip install -r requirements.txt
```

## Setup
1. Get a Hugging Face API token from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).
2. *Either*:
   - **Option 1**: Create a `.env` file with:
     ```python
     HUGGINGFACEHUB_API_TOKEN=your_token_here
     ```
   - **Option 2**: For Streamlit Sharing, add the token to `st.secrets` under `HUGGINGFACE_API_TOKEN`.

## Models Used
- Embeddings: `sentence-transformers/all-MiniLM-L6-v2`
- Text Generation: `google/flan-t5-base`


## Usage
```bash
(venv) $ streamlit run app.py
```
Navigate to <http://localhost:8501>, upload one or more `.txt` documents, then enter questions such as:
* *“What is the attendance policy?”*
* *“When is the final exam?”*

The answer section will display context‑aware replies extracted from your uploads.

## Data Requirements
* **Input format:** Plain‑text (`.txt`) files.  Convert PDFs/Word docs beforehand.
* **Chunk size:** ~500 tokens with 20 token overlap (configurable in code).
* **Index persistence:** FAISS index is kept in‑memory each session; add persistence if desired.

## Testing
Automated tests are not yet included.  Manual smoke test:
1. Run the app.
2. Upload `canvas_docs.txt` (sample file).
3. Ask *“What topics are in Week 3?”* → verify a sensible answer.

Planned: `pytest` unit tests for embedding & retrieval functions and a CI workflow.

## Configuration
Key options live in **`app.py`**:
| Setting | Default | Description |
|---------|---------|-------------|
| `model` | `google/flan-t5-base` | Generation model |
| `chunk_size` | 500 | Tokens per chunk |
| `vector_store` | FAISS | Swap for Chroma, Weaviate, etc. |
| `temperature` | 0.5 | Generation creativity |

## Methodology
1. **Load & Chunk Docs** – LangChain `TextLoader` + `RecursiveCharacterTextSplitter`.
2. **Embed** – `sentence-transformers/all-MiniLM-L6-v2` via `HuggingFaceEmbeddings`.
3. **Index** – vectors stored in FAISS for ANN lookup.
4. **Retrieve** – top‑k similarity search (`k=4`).
5. **Generate** – retrieved context + user query passed to Flan‑T5.
6. **Serve** – Streamlit UI orchestrates the full pipeline.

## Performance
| Metric | Value | Notes |
|--------|-------|-------|
| Avg. retrieval latency | < 300 ms on CPU | 200 docs, i7‑1185G7 |
| End‑to‑end response | ~2–3 s | Flan‑T5 base on CPU |

For larger corpora or lower latency, enable GPU or switch to a distilled model.

## License
This project is released under the **Hugging Face License** – free for non‑commercial or educational use.  See `LICENSE` for full terms.

## Contributing
Pull requests are welcome!  Please:
1. Fork the repo and create a feature branch.
2. Follow PEP 8 style and write docstrings.
3. Add/adjust tests where relevant.
4. Open a PR with a clear description.

## Changelog
| Date | Version | Notes |
|------|---------|-------|
| 2025‑06‑16 | 1.0.0 | Initial public release |

## Citation
If you use this code in academic work, please cite:
```bibtex
@misc{stockdale2025canvasrag,
  title        = {Canvas LMS RAG Chatbot},
  author       = {Stockdale, Myrah},
  year         = {2025},
  howpublished = {GitHub},
  url          = {https://github.com/Myrahrs/Foundations-of-Agentic-AI}
}
```

## Contact
**Maintainer:** Myrah Stockdale  
Email: *myrah.stockdale@gmail.com*

