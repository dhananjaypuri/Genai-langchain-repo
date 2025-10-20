# Embedding

This folder contains examples of using OpenAI embeddings with LangChain. Embeddings are vector representations of text that capture semantic meaning and are commonly used for similarity search, clustering, and other machine learning tasks.

## Files

### 01_openai_single_emb.py
Demonstrates how to generate embeddings for a single text query using OpenAI's embedding model.

**Features:**
- Uses OpenAI's ChatOpenAI for text generation
- Uses OpenAI's text-embedding-3-small model for embeddings
- Generates a 32-dimensional vector embedding
- Shows how to embed a single query string

**Dependencies:**
- `langchain_openai`
- `python-dotenv`

**Usage:**
```bash
python 01_openai_single_emb.py
```

**Environment Variables Required:**
- `OPENAI_API_KEY` - Your OpenAI API key

**What it does:**
1. Generates text using ChatOpenAI
2. Creates an embedding of the generated text using `embed_query()`
3. Prints the resulting vector representation

### 02_openai_document_embed.py
Demonstrates how to generate embeddings for multiple documents using OpenAI's embedding model.

**Features:**
- Uses OpenAI's text-embedding-3-small model for embeddings
- Generates 32-dimensional vector embeddings
- Shows how to embed multiple documents at once
- Includes example output showing the vector format

**Dependencies:**
- `langchain_openai`
- `python-dotenv`

**Usage:**
```bash
python 02_openai_document_embed.py
```

**Environment Variables Required:**
- `OPENAI_API_KEY` - Your OpenAI API key

**What it does:**
1. Defines a list of document strings
2. Creates embeddings for all documents using `embed_documents()`
3. Prints the resulting vector representations

## Setup

1. Install the required dependencies:
```bash
pip install -r ../requirement.txt
```

2. Create a `.env` file in the parent directory with your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

3. Run any of the example files:
```bash
python 01_openai_single_emb.py
python 02_openai_document_embed.py
```

## Key Differences

- **`embed_query()`**: Used for single text strings (queries, search terms)
- **`embed_documents()`**: Used for multiple documents (batch processing)

## Embedding Model Details

- **Model**: `text-embedding-3-small`
- **Dimensions**: 32 (configurable)
- **Use Cases**: Semantic search, document similarity, clustering, recommendation systems

## Notes

- The `.env` file should be placed in the parent directory (`../`) relative to this folder
- Make sure you have a valid OpenAI API key before running the examples
- Embeddings are returned as lists of floating-point numbers representing the vector
- The 32-dimensional vectors shown in the examples are just a subset for demonstration
- Higher dimensions generally provide better accuracy but at higher cost
