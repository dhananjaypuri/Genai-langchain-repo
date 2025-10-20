# LLMs

This folder contains examples of using Language Learning Models (LLMs) with LangChain. The examples demonstrate how to set up and use different LLM providers for text generation tasks.

## Files

### 01_llm.py
Demonstrates how to use OpenAI's basic LLM model with LangChain.

**Features:**
- Uses OpenAI's GPT-4.1-nano model
- Loads environment variables from `.env` file
- Simple text generation example
- Direct text output (no additional formatting)

**Dependencies:**
- `langchain_openai`
- `python-dotenv`

**Usage:**
```bash
python 01_llm.py
```

**Environment Variables Required:**
- `OPENAI_API_KEY` - Your OpenAI API key

## Setup

1. Install the required dependencies:
```bash
pip install -r ../requirement.txt
```

2. Create a `.env` file in the parent directory with your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

3. Run the example file:
```bash
python 01_llm.py
```

## Difference between LLMs and ChatModels

- **LLMs**: Basic text generation models that take a string input and return a string output
- **ChatModels**: Specialized for conversational AI, they take a list of messages and return a message object with additional metadata

## Notes

- The example asks "What is the capital of India?" to demonstrate text generation
- The `.env` file should be placed in the parent directory (`../`) relative to this folder
- Make sure you have a valid OpenAI API key before running the example
- The output is printed directly without additional formatting (unlike ChatModels which return structured message objects)
