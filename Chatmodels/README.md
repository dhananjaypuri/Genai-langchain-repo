# Chatmodels

This folder contains examples of using different chat models with LangChain. Each file demonstrates how to set up and use a specific chat model provider.

## Files

### 01_chatmodel.py
Demonstrates how to use OpenAI's ChatOpenAI model with LangChain.

**Features:**
- Uses OpenAI's GPT-4.1-nano model
- Loads environment variables from `.env` file
- Simple question-answering example

**Dependencies:**
- `langchain_openai`
- `python-dotenv`

**Usage:**
```bash
python 01_chatmodel.py
```

**Environment Variables Required:**
- `OPENAI_API_KEY` - Your OpenAI API key

### 02_google.py
Demonstrates how to use Google's ChatGoogleGenerativeAI model with LangChain.

**Features:**
- Uses Google's Gemini-2.5-flash model
- Loads environment variables from `.env` file
- Simple question-answering example

**Dependencies:**
- `langchain_google_genai`
- `python-dotenv`

**Usage:**
```bash
python 02_google.py
```

**Environment Variables Required:**
- `GOOGLE_API_KEY` - Your Google AI API key

## Setup

1. Install the required dependencies:
```bash
pip install -r ../requirement.txt
```

2. Create a `.env` file in the parent directory with your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

3. Run any of the example files:
```bash
python 01_chatmodel.py
python 02_google.py
```

## Notes

- Both examples ask the same question ("What is the capital of India?") to demonstrate the different model responses
- The `.env` file should be placed in the parent directory (`../`) relative to this folder
- Make sure you have valid API keys for the respective services before running the examples

