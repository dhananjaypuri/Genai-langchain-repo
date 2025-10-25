# Simple Chatbot

A basic conversational chatbot built using LangChain and OpenAI's GPT model.

## Overview

This chatbot provides a simple command-line interface for interacting with OpenAI's GPT-4.1-nano model. It allows users to have continuous conversations until they decide to exit.

## Features

- **Interactive CLI**: Simple command-line interface for user interaction
- **OpenAI Integration**: Uses OpenAI's GPT-4.1-nano model via LangChain
- **Continuous Conversation**: Maintains conversation flow until user exits
- **Easy Exit**: Type "exit" or "bye" to end the conversation

## Prerequisites

- Python 3.7+
- OpenAI API key
- Required Python packages (see requirements below)

## Installation

1. Install the required dependencies:
```bash
pip install langchain-openai python-dotenv
```

2. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

## Usage

Run the chatbot:
```bash
python 01_chatbot.py
```

Start chatting! Type your messages and press Enter. To exit, type "exit" or "bye".

## Code Structure

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.7)

while True:
    user_input = input("You : ")
    if user_input == "exit" or user_input == "bye":
        break
    response = model.invoke(user_input)
    print(f"AI : {response.content}")
```

## Configuration

- **Model**: GPT-4.1-nano
- **Temperature**: 0.7 (controls randomness in responses)
- **Exit Commands**: "exit" or "bye"

## Drawbacks and Limitations

### **Memory Issue - No Conversation Context**
The chatbot has a critical limitation regarding conversation memory:

- **No Conversation Memory**: The chatbot doesn't remember previous messages in the conversation
- **Lost Context**: Each interaction is treated as a standalone request, so context from earlier messages is completely lost
- **Stateless Design**: The AI model receives only the current user input without any conversation history
- **Poor User Experience**: Users cannot reference previous parts of the conversation or build upon earlier topics
- **No Continuity**: The chatbot cannot maintain coherent, multi-turn conversations

**Example of the problem:**
```
User: "My name is John and I like pizza"
AI: "Nice to meet you! Pizza is great."
User: "What's my name and what do I like?"
AI: "I don't have any information about your name or preferences."
```

This memory limitation makes the chatbot unsuitable for any application requiring context awareness or multi-turn conversations.

## Potential Improvements

1. **Add conversation memory** using LangChain's memory modules
2. **Implement error handling** for robust operation
3. **Add input validation** and sanitization
4. **Create configuration system** for easy customization
5. **Add conversation logging** and history management
6. **Implement streaming responses** for better UX
7. **Add system prompts** for role-based conversations
8. **Include security measures** against prompt injection

## Dependencies

- `langchain-openai`: LangChain integration with OpenAI
- `python-dotenv`: Environment variable management

## License

This project is part of a learning tutorial and is for educational purposes.
