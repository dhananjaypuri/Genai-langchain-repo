# LangChain Generative AI Tutorial

A comprehensive tutorial covering various aspects of LangChain and Generative AI, including chatbots, embeddings, prompt engineering, and different AI model integrations.

## 📚 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Topics Covered](#topics-covered)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Learning Path](#learning-path)

## 🎯 Overview

This project is a hands-on tutorial for learning LangChain and Generative AI concepts. It covers everything from basic LLM interactions to advanced prompt engineering, embeddings, and semantic search. Each folder contains practical examples with detailed explanations.

## 📁 Project Structure

```
gen-ai/
├── Chatbot/                          # Basic chatbot implementations
│   ├── 01_chatbot.py                # Simple chatbot without memory
│   └── README.md                    # Chatbot documentation
├── Chatmodels/                      # Different chat model integrations
│   ├── 01_chatmodel.py             # OpenAI ChatOpenAI example
│   ├── 02_google.py                # Google Gemini integration
│   └── README.md                   # Chat models documentation
├── Embedding/                       # Text embedding examples
│   ├── 01_openai_single_emb.py     # Single text embedding
│   ├── 02_openai_document_embed.py # Document embedding
│   └── README.md                   # Embedding documentation
├── HuggingFModels/                  # Hugging Face model integration
│   ├── 01_hf.py                    # Hugging Face endpoint example
│   └── 02_hf.py                    # Additional HF examples
├── LLMs/                           # Large Language Model basics
│   ├── 01_llm.py                   # Basic LLM usage
│   └── README.md                   # LLM documentation
├── Messages/                        # Message-based conversations
│   ├── 01_chatbot_with_history.py  # Chatbot with conversation memory
│   ├── messages/                   # Message handling examples
│   │   ├── 01_simple_messages.py   # Basic message structure
│   │   └── 02_chatbot_with_history_using_messages.py
│   └── README.md                   # Messages documentation
├── Prompts/                        # Prompt engineering
│   ├── chat-prompt-templates/      # Chat prompt templates
│   │   ├── 01_chat.py             # Role-based chat prompts
│   │   └── README.md              # Chat templates documentation
│   └── PromptTemplate/             # Traditional prompt templates
│       ├── 01_static_prompt.py    # Static prompt example
│       ├── 02_dynamic_prompt.py   # Dynamic prompt with Streamlit
│       ├── 03_save_template.py    # Save prompt templates
│       ├── 04_load_prompt_template.py # Load saved templates
│       └── template.json          # Saved template file
├── Symentic Search/                # Semantic search implementation
│   └── 01_embedding.py            # Cosine similarity search
├── requirement.txt                 # Project dependencies
└── README.md                      # This file
```

## 🎓 Topics Covered

### 1. **Large Language Models (LLMs)**
- **Location**: `LLMs/`
- **Topics**: Basic LLM usage, OpenAI integration
- **Key Concepts**: Model invocation, response handling
- **Examples**: Simple question-answering with GPT models

### 2. **Chat Models**
- **Location**: `Chatmodels/`
- **Topics**: Chat-specific model interfaces, multiple provider support
- **Key Concepts**: ChatOpenAI, Google Gemini integration
- **Examples**: Conversational AI with different model providers

### 3. **Text Embeddings**
- **Location**: `Embedding/`
- **Topics**: Text vectorization, similarity search
- **Key Concepts**: OpenAI embeddings, single vs document embedding
- **Examples**: Converting text to vectors for semantic analysis

### 4. **Message-Based Conversations**
- **Location**: `Messages/`
- **Topics**: Structured conversations, conversation memory
- **Key Concepts**: SystemMessage, HumanMessage, AIMessage
- **Examples**: Multi-turn conversations with context preservation

### 5. **Prompt Engineering**
- **Location**: `Prompts/`
- **Topics**: Template creation, dynamic prompts, role-based prompting
- **Key Concepts**: PromptTemplate, ChatPromptTemplate, variable substitution
- **Examples**: Static prompts, dynamic prompts with Streamlit UI

### 6. **Chatbot Development**
- **Location**: `Chatbot/`
- **Topics**: Interactive chatbots, conversation loops
- **Key Concepts**: User input handling, response generation
- **Examples**: Basic chatbot without memory, chatbot with conversation history

### 7. **Hugging Face Integration**
- **Location**: `HuggingFModels/`
- **Topics**: Open-source model integration
- **Key Concepts**: HuggingFaceEndpoint, model hosting
- **Examples**: Using Llama models through Hugging Face

### 8. **Semantic Search**
- **Location**: `Symentic Search/`
- **Topics**: Vector similarity, document retrieval
- **Key Concepts**: Cosine similarity, embedding-based search
- **Examples**: Finding relevant documents using semantic similarity

## 🛠 Prerequisites

- Python 3.7+
- OpenAI API key
- Google API key (for Gemini examples)
- Hugging Face API key (for HF examples)
- Basic understanding of Python programming

## 📦 Installation

1. **Clone the repository**:
```bash
git clone <repository-url>
cd gen-ai
```

2. **Install dependencies**:
```bash
pip install -r requirement.txt
```

3. **Set up environment variables**:
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
```

## 🚀 Usage

### Quick Start
1. Navigate to any folder of interest
2. Read the specific README.md for detailed instructions
3. Run the Python files to see examples in action

### Example Workflow
```bash
# Start with basic LLM
cd LLMs
python 01_llm.py

# Try embeddings
cd ../Embedding
python 01_openai_single_emb.py

# Build a chatbot
cd ../Chatbot
python 01_chatbot.py

# Advanced: Semantic search
cd "../Symentic Search"
python 01_embedding.py
```

## 📋 Dependencies

The project uses the following key dependencies:

### Core LangChain
- `langchain` - Core LangChain framework
- `langchain-core` - Core LangChain functionality

### Model Integrations
- `langchain-openai` - OpenAI integration
- `langchain-google-genai` - Google Gemini integration
- `langchain-huggingface` - Hugging Face integration
- `langchain-anthropic` - Anthropic Claude integration

### Utilities
- `python-dotenv` - Environment variable management
- `streamlit` - Web UI for interactive examples
- `numpy` - Numerical computations
- `scikit-learn` - Machine learning utilities (cosine similarity)
- `transformers` - Hugging Face transformers
- `huggingface-hub` - Hugging Face model hub

## 🗺 Learning Path

### Beginner Level
1. **LLMs** - Start with basic language model usage
2. **Chatmodels** - Learn about chat-specific interfaces
3. **Basic Chatbot** - Build your first interactive chatbot

### Intermediate Level
4. **Messages** - Understand structured conversations
5. **Prompt Templates** - Learn prompt engineering basics
6. **Embeddings** - Explore text vectorization

### Advanced Level
7. **Chat Prompt Templates** - Advanced prompt engineering
8. **Semantic Search** - Implement vector-based search
9. **Hugging Face Models** - Work with open-source models

### Expert Level
10. **Memory Management** - Implement conversation persistence
11. **Error Handling** - Add robust error management
12. **Production Deployment** - Scale for production use

## 🎯 Key Learning Outcomes

After completing this tutorial, you will understand:

- **LangChain Architecture**: How LangChain components work together
- **Model Integration**: How to integrate different AI model providers
- **Prompt Engineering**: Best practices for creating effective prompts
- **Conversation Management**: How to maintain context in conversations
- **Vector Operations**: How to work with text embeddings and similarity
- **Semantic Search**: How to implement intelligent document retrieval
- **Error Handling**: How to build robust AI applications

## 🔧 Customization

Each example is designed to be easily customizable:

- **Model Selection**: Change models by modifying the model parameter
- **Temperature Control**: Adjust creativity with temperature settings
- **Template Variables**: Modify prompts to suit your use case
- **UI Components**: Customize Streamlit interfaces for your needs

## 📖 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Hugging Face Documentation](https://huggingface.co/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)

## 🤝 Contributing

This is a learning tutorial. Feel free to:
- Add more examples
- Improve existing code
- Fix bugs
- Add documentation

## 📄 License

This project is for educational purposes. Please ensure you comply with the terms of service of the AI model providers you use.

---

**Happy Learning! 🚀**

Start with the `LLMs/` folder and work your way through each topic to build a comprehensive understanding of LangChain and Generative AI.

