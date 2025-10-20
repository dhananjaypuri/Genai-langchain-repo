# Semantic Search (Symentic Search)

This folder contains a minimal example of building a simple semantic search using OpenAI embeddings and cosine similarity.

## What the example does

- Embeds a small list of festival-related documents using OpenAI's `text-embedding-3-small` model (32 dimensions)
- Embeds a user query string using the same model
- Computes cosine similarity between the query vector and each document vector
- Returns the most semantically similar document to the query

## File

- `01_embedding.py`: End-to-end example of embedding a query and documents, then ranking with cosine similarity.

## Setup

1. Install dependencies
```bash
pip install -r ../requirement.txt
```
If you don't have scikit-learn yet:
```bash
pip install scikit-learn
```

2. Create a `.env` file one level up (in the `gen-ai` folder) and add your key:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

Run the script:
```bash
python 01_embedding.py
```

You should see output similar to:
- A printed vector for the embedded query
- Printed vectors for each embedded document
- The single most similar document printed at the end

## How it works (quick reference)

- Embedding model: `text-embedding-3-small` with 32 dimensions
- `embed_query(query)`: converts the query to a vector
- `embed_documents(documents)`: converts each document to a vector
- `cosine_similarity(query_vector, document_vectors)`: measures similarity in vector space
- Highest similarity score indicates the best-matching document

## Dependencies
- `langchain_openai`
- `python-dotenv`
- `scikit-learn` (for cosine similarity)
- `numpy`

## Notes
- Ensure the `.env` file is placed in the parent directory so `load_dotenv()` can find it
- The example uses a small embedding dimension (32) for readability; higher dimensions improve quality at higher cost
