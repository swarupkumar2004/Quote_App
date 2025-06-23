import streamlit as st
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

df = pd.read_csv("english_quotes_cleaned.csv")
model = SentenceTransformer("all-MiniLM-L6-v2")

quotes = df['quote'].tolist()
quote_embeddings = model.encode(quotes)
dimension = quote_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(quote_embeddings))

def search_quotes(query, author_filter=None, k=50):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k)

    results = []
    for i in I[0]:
        quote = df.iloc[i]['quote']
        author = df.iloc[i]['author']
        tags = df.iloc[i]['tags']

        if author_filter:
            if author_filter.lower() not in author.lower():
                continue

        results.append({
            "quote": quote,
            "author": author,
            "tags": tags
        })
        if len(results) >= 5:
            break

    if author_filter and len(results) == 0:
        fallback_df = df[df['author'].str.lower().str.contains(author_filter.lower())]
        fallback = fallback_df.sample(min(5, len(fallback_df)))
        for _, row in fallback.iterrows():
            results.append({
                "quote": row['quote'],
                "author": row['author'],
                "tags": row['tags']
            })

    return results

st.title("@ Semantic Quote Retriever")
#st.markdown("Built for **Vijayi AI Internship Task 2** using FAISS + MiniLM + RAG pipeline.")

query = st.text_input("Enter your query :)", "")
author = st.text_input("Optional:Author Name :)", "")

if st.button("Search"):
    if query.strip() == "":
        st.warning("Please enter a query.")
    else:
        results = search_quotes(query, author_filter=author)
        if not results:
            st.error("No matching quotes found.")
        else:
            for i, res in enumerate(results, 1):
                st.markdown(f"---\n** Result {i}**")
                st.write(f"Quote: *{res['quote']}*")
                st.write(f"Author: `{res['author']}`")
                st.write(f"Tags: {res['tags']}")
