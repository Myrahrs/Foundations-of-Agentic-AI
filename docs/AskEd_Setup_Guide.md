
# 🤖 AskEd Chatbot Setup Guide

Welcome to **AskEd**, your AI assistant for answering questions about Canvas LMS and AI coursework. This guide will help you set up the AskEd chatbot using **Streamlit**, **LangChain**, and **Hugging Face**.

---

## 📌 Prerequisites

### ✅ Install Python (If Not Installed)
- **Windows**: Download from [python.org](https://www.python.org/downloads/)
- **Mac/Linux**: Usually pre-installed. Check with:
  ```sh
  python3 --version
  ```

### ✅ Install Git (Optional but Recommended)
- Download from [git-scm.com](https://git-scm.com/)
- Verify with:
  ```sh
  git --version
  ```

### ✅ Obtain a Hugging Face API Key
1. Sign up at [Hugging Face](https://huggingface.co/join)
2. Go to your **Settings → Access Tokens**
3. Generate a new token (read access is sufficient)
4. Save it in a file named `.streamlit/secrets.toml`:
   ```toml
   HUGGINGFACE_API_TOKEN = "your-token-here"
   ```

---

## 🚀 Installation Steps

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Myrahrs/Foundations-of-Agentic-AI.git
cd Foundations-of-Agentic-AI
git checkout AAIDC-Module-1-Project
```

### 2️⃣ Create a Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Chatbot Locally
```sh
streamlit run src_assets/app.py
```

---

## 🔹 Optional Parameters & Features

| Feature | Description |
|--------|-------------|
| `canvas_docs.txt` | Custom knowledge file for Canvas LMS, loaded from GitHub or local `data/` folder |
| `flan-t5-base` | Uses this open-source Hugging Face model for question answering |
| `temperature` | Set in `model_kwargs` for controlling response creativity (default: 0.5) |

---

## 🛠 Next Steps

- Test questions like:
  - "How do I reset my Canvas password?"
  - "Where can I find the course syllabus?"
- Update `canvas_docs.txt` with your own knowledge base
- Share a live demo using tools like Streamlit Cloud or Render
- Create a QR code linking to your app demo (optional)
- Link to the [Troubleshooting Guide](AskEd_Troubleshooting_Guide.md)

---

🚀 **AskEd is now ready to assist your learners!**
