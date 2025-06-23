# Quote_App
```markdown
# 🧠 Semantic Quote Retriever

This project implements a **Retrieval-Augmented Generation (RAG)**-style quote search system using the [Abirate/english_quotes](https://huggingface.co/datasets/Abirate/english_quotes) dataset.

> ✅ Built using **Sentence Transformers + FAISS + Streamlit**

---

## 🔍 Problem Statement

**Goal:**  
Build a semantic search engine that returns relevant quotes based on a user query, with optional author filtering.

**Tasks Completed:**
- Data preprocessing & cleaning
- Embedding using `all-MiniLM-L6-v2`
- FAISS index creation for fast vector search
- Semantic search with optional author filter
- Fallback to author-based quotes if no match
- Streamlit UI for interactive input/output

---

## 📂 Project Structure

```

.
├── english\_quotes\_cleaned.csv   # Cleaned dataset
├── app.py                       # Streamlit web app
├── README.md                    # You're here

````

---

## 🚀 How to Run

### 🔧 Install Required Libraries

```bash
pip install streamlit sentence-transformers faiss-cpu pandas numpy
````

### ▶️ Launch the App

```bash
python -m streamlit run app.py / streamlit run app.py
```

Visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## ✨ Features

* 🔍 **Semantic quote search** using embeddings
* 👤 **Optional author filter** (e.g. "Helen Keller")
* 🔁 **Fallback** to author's random quotes if no semantic match
* 🎨 Clean Streamlit UI

---

## 🧪 Example Usage

**Input Query:**

```
hope and strength
Author: Helen Keller
```

**Output:**

* Shows 5 relevant quotes by Helen Keller
* Or shows fallback if semantic match not found

---

## 📚 Dataset

Used the [Abirate/english\_quotes](https://huggingface.co/datasets/Abirate/english_quotes) dataset from Hugging Face, filtered and cleaned to remove missing values and long entries.

---

## 🛠 Tools Used

* `sentence-transformers` for text embeddings
* `faiss-cpu` for similarity search
* `streamlit` for web interface
* `pandas`, `numpy` for preprocessing

🟢 Ready to paste directly into your `README.md` file.

Bol agar:
- `haan video script bhi de do` 🎥
- ya `task 1 ka readme bhi chahiye` 📄
```
