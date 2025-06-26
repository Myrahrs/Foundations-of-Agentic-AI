
# 🛠️ AskEd Troubleshooting Guide

## 🔹 Common Issues & Fixes

---

### ❌ API Key Not Found  
**Issue:**  
The app fails to run or crashes with a Hugging Face API error.

**Fix:**  
- Make sure you’ve added your Hugging Face API key to `.streamlit/secrets.toml`:  
  ```toml
  HUGGINGFACE_API_TOKEN = "your-key-here"
  ```
- If running locally, also ensure your environment includes:
  ```bash
  export HUGGINGFACE_API_TOKEN="your-key-here"
  ```

---

### ❌ Dependencies Not Installed  
**Issue:**  
Missing package errors like `ModuleNotFoundError`.

**Fix:**  
Install all required dependencies using:
```bash
pip install -r requirements.txt
```

---

### ❌ File Not Found or Incorrect Path  
**Issue:**  
The app crashes trying to load `canvas_docs.txt`.

**Fix:**  
- Ensure `canvas_docs.txt` is present in the `data/` folder.
- If hosted remotely (e.g., GitHub), confirm the link is correct and the file is public.
- If using a temporary file loader, ensure the download succeeded before loading.

---

### ❌ File Format Issues  
**Issue:**  
The app can't load or parse the knowledge base documents.

**Fix:**  
- Supported format: plain text `.txt`.
- Ensure clean formatting—no extra encoding, markdown, or embedded metadata.
- If using Google Docs or Word, export as `.txt` before upload.

---

### ❌ Blank or Nonsensical Responses  
**Issue:**  
AskEd provides vague, incomplete, or off-topic answers.

**Fix:**  
- Check the quality of your source document (`canvas_docs.txt`).
- Revise your question to be more specific or context-rich.
- Try increasing `max_length` or adjusting `temperature` in `model_kwargs`.

---

### ❌ API Rate Limits or Timeouts  
**Issue:**  
Hugging Face model stalls, or Streamlit shows timeout/rate limit errors.

**Fix:**  
- Reduce the number of concurrent users or refresh rate.
- Use CPU-efficient models (e.g., `flan-t5-base` is a good balance).
- Consider upgrading your Hugging Face plan if rate-limited.

---

### ❌ General Debugging Tips  
- Use `st.spinner()` and `try/except` to catch errors gracefully.
- Print file paths and directory contents with `os.getcwd()` and `os.listdir()` for debugging.
- Check **Streamlit logs** (Cloud → Manage App → Logs) for full traceback info.

---

### ❌ Still Stuck?  
- 🧠 Check [GitHub Issues](https://github.com/Myrahrs/Foundations-of-Agentic-AI/issues)
- 🛠️ Submit a new issue with:
  - Error message
  - Environment (local/cloud)
  - Steps to reproduce

---

### 🚀 Follow these steps, and AskEd should work smoothly!
