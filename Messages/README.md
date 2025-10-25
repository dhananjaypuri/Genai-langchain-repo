# Chatbot with Conversation History

An improved conversational chatbot that maintains conversation context and history using LangChain and OpenAI's GPT model.

## Overview

This chatbot addresses the memory limitation of the basic chatbot by implementing conversation history tracking. It maintains both a simple message list and a structured history for better conversation continuity.

## Features

- **Conversation Memory**: Maintains context throughout the conversation
- **Dual History Tracking**: Both simple messages array and structured history object
- **Context Awareness**: AI can reference previous parts of the conversation
- **Interactive CLI**: Simple command-line interface for user interaction
- **OpenAI Integration**: Uses OpenAI's GPT-4.1-nano model via LangChain
- **Conversation Logging**: Displays full conversation history at the end

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
python 01_chatbot_with_history.py
```

Start chatting! The AI will now remember your previous messages. To exit, type "exit" or "bye".

## Code Structure

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.7)
messages = []
history = []

while True:
    user_input = input("You : ")
    if user_input == "exit" or user_input == "bye":
        break
    messages.append(user_input)
    history.append({'user': user_input})
    response = model.invoke(messages)
    
    print(f"AI : {response.content}")
    messages.append(response.content)
    history.append({'ai': response.content})

print(messages)
print(history)
```

## Configuration

- **Model**: GPT-4.1-nano
- **Temperature**: 0.7 (controls randomness in responses)
- **Exit Commands**: "exit" or "bye"
- **Memory**: Maintains full conversation history

## Pros and Cons

### ✅ **Pros**

#### 1. **Conversation Memory**
- **Context Awareness**: AI remembers previous messages and can reference them
- **Multi-turn Conversations**: Supports coherent, continuous conversations
- **Better User Experience**: Users can build upon previous topics naturally

#### 2. **Dual History Tracking**
- **Simple Messages Array**: Easy to pass to the AI model
- **Structured History**: Organized format for logging and analysis
- **Flexible Data Structure**: Can be easily extended for different use cases

#### 3. **Improved Functionality**
- **Conversation Continuity**: Maintains context throughout the session
- **Reference Capability**: AI can answer questions about earlier parts of the conversation
- **Natural Interaction**: Feels more like talking to a real person

#### 4. **Debugging Support**
- **Full Logging**: Displays complete conversation at the end
- **Easy Troubleshooting**: Can see exactly what was sent to the AI
- **Development Aid**: Helps understand conversation flow

### ❌ **Cons**

#### 1. **Memory Management Issues**
- **Unlimited Growth**: Messages array grows indefinitely without limits
- **Token Limit Risk**: May exceed model's context window with long conversations
- **Memory Leak**: No cleanup mechanism for old conversations
- **Performance Degradation**: Slower responses as conversation gets longer

#### 2. **No Error Handling**
- **API Failures**: No handling for OpenAI API errors or rate limits
- **Network Issues**: Will crash on connection problems
- **Input Validation**: No protection against malformed inputs

#### 3. **Limited Memory Strategy**
- **No Memory Optimization**: Doesn't use LangChain's built-in memory modules
- **Inefficient Storage**: Stores raw strings instead of proper message objects
- **No Memory Persistence**: History is lost when program exits

#### 4. **Security Concerns**
- **No Input Sanitization**: Vulnerable to prompt injection attacks
- **No Rate Limiting**: No protection against abuse
- **Memory Exposure**: Full conversation history printed to console

#### 5. **User Experience Issues**
- **No Loading Indicators**: No feedback during API calls
- **Console Clutter**: History printing at the end clutters the interface
- **No Response Formatting**: Raw text output without formatting

#### 6. **Scalability Problems**
- **Session-based Only**: No persistence across sessions
- **Single User**: No multi-user support
- **No Memory Management**: No strategy for handling long conversations

## Example Conversation

```
You : My name is John and I like pizza
AI : Nice to meet you, John! Pizza is a great choice. What's your favorite type of pizza?

You : What's my name and what do I like?
AI : Your name is John and you like pizza! You mentioned that in our previous conversation.

You : Can you recommend a pizza place?
AI : I'd be happy to help you find a pizza place! Since you like pizza, what type of pizza do you prefer? Are you looking for something specific like thin crust, deep dish, or a particular style?
```

## Potential Improvements

1. **Implement LangChain Memory Modules**: Use ConversationBufferWindowMemory or ConversationSummaryMemory
2. **Add Memory Limits**: Implement conversation length limits to prevent token overflow
3. **Error Handling**: Add try-catch blocks for robust operation
4. **Input Validation**: Sanitize and validate user inputs
5. **Memory Persistence**: Save conversation history to files or database
6. **Memory Optimization**: Use proper message objects and memory management
7. **Security Measures**: Add input sanitization and rate limiting
8. **Better UX**: Add loading indicators and response formatting

## Dependencies

- `langchain-openai`: LangChain integration with OpenAI
- `python-dotenv`: Environment variable management

## License

This project is part of a learning tutorial and is for educational purposes.


