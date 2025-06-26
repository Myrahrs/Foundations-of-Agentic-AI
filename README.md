
# 📘 Canvas LMS Chatbot – AskEd 🚀  
A lightweight, local RAG chatbot that answers questions about Canvas LMS course documents using LangChain + Hugging Face models.

---

## ✨ Features  
✅ Upload and query **Canvas syllabi, schedules, and policies**  
✅ Uses **FAISS for fast vector search**  
✅ Retrieval-Augmented Generation powered by **Flan-T5**  
✅ Built with **LangChain**, **Hugging Face**, and **Streamlit**  
✅ No external database or cloud storage needed  
✅ Clean **local deployment** and Streamlit UI  
✅ QR code access for live demos  

---

## 📌 Getting Started  

### **1️⃣ Install Dependencies**  
You'll need **Python 3.10+** and a Hugging Face API key.

#### **Terminal**
```bash
git clone https://github.com/Myrahrs/Foundations-of-Agentic-AI.git
cd Foundations-of-Agentic-AI
git checkout AAIDC-Module-1-Project
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### **2️⃣ Set Up Your Hugging Face API Key**  
1. Sign up at **[Hugging Face](https://huggingface.co/join)**  
2. Go to **Settings → Access Tokens**  
3. Create a token and save it in:  
   - For local dev: `.env` file  
     ```env
     HUGGINGFACEHUB_API_TOKEN=your_token_here
     ```
   - For Streamlit Cloud: `.streamlit/secrets.toml`  
     ```toml
     HUGGINGFACE_API_TOKEN = "your_token_here"
     ```

---

### **3️⃣ Run the AskEd Chatbot**  
```bash
streamlit run src_assets/app.py
```

Once the app starts, visit: [http://localhost:8501](http://localhost:8501)  
Upload your `.txt` Canvas files and ask questions like:  
*“What are the late submission penalties?”*  
*“When is the Week 4 quiz?”*

---

## 🔍 Customization  

| Component | Location | Description |
|----------|----------|-------------|
| 📄 Document Input | `data/canvas_docs.txt` | Source text for chatbot context |
| 🧠 Embeddings | `sentence-transformers/all-MiniLM-L6-v2` | Used for FAISS vector indexing |
| ✍️ Generator Model | `google/flan-t5-base` | Used for answer generation |
| 🔧 Config | `app.py` | Chunk size, retriever settings, model kwargs |

You can swap in different models, vector stores, or add persistence.

---

## 🧪 Testing & Demo  
1. Load the app  
2. Upload a sample file  
3. Ask a Canvas-related question  

Include a QR code in documentation or slides for quick demo access.

---

## 🛠 Troubleshooting  
Check out the [Troubleshooting Guide](AskEd_Troubleshooting_Guide.md) for help with:  
- API key errors  
- Missing packages  
- Model loading failures  
- Empty or irrelevant responses  

---

## 📜 License  
**Hugging Face License** – Free for educational/non-commercial use. See `LICENSE` for terms.

---

## 🎤 Contributions  
Pull requests and ideas welcome!  
1. Fork the repo  
2. Follow PEP8 and docstring guidelines  
3. Open a PR with clear description  

---

## 📅 Changelog  
| Date | Version | Notes |
|------|---------|-------|
| 2025‑06‑16 | 1.0.0 | Initial release of AskEd |

---

## 📚 Citation  
```bibtex
@misc{stockdale2025canvasrag,
  title        = {Canvas LMS RAG Chatbot},
  author       = {Stockdale, Myrah},
  year         = {2025},
  howpublished = {GitHub},
  url          = {https://github.com/Myrahrs/Foundations-of-Agentic-AI}
}
```

---

## 📬 Contact  
**Maintainer:** Myrah Stockdale  
Email: *myrah.stockdale@gmail.com*
