# Chat Prompt Templates

A demonstration of using LangChain's ChatPromptTemplate for structured conversations with role-based messaging.

## Overview

This example showcases how to create structured chat prompts using LangChain's ChatPromptTemplate and ChatMessagePromptTemplate. It demonstrates role-based messaging with system and human roles, and shows how to use the LangChain chain pattern for streamlined execution.

## Features

- **Role-based Messaging**: Uses system and human roles for structured conversations
- **Template Variables**: Dynamic content injection using template variables
- **LangChain Chains**: Demonstrates the chain pattern for streamlined execution
- **Structured Prompts**: Organized prompt structure with clear role separation
- **Variable Substitution**: Easy parameterization of prompts

## Prerequisites

- Python 3.7+
- OpenAI API key
- Required Python packages (see requirements below)

## Installation

1. Install the required dependencies:
```bash
pip install langchain-openai langchain-core python-dotenv
```

2. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

## Usage

Run the chat prompt template:
```bash
python 01_chat.py
```

The script will execute a predefined prompt asking about AWS Bedrock from an AWS expert perspective.

## Code Structure

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, ChatMessagePromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)

template = ChatPromptTemplate([
    ('system', 'You are a {domain} expert'),
    ('human', "Tell me about {topic}")
])

# Method 1: Manual invocation (commented out)
# prompt = template.invoke({'domain': 'AWS', 'topic': 'Bedrock'})
# response = model.invoke(prompt)
# print(response.content)

# Method 2: Using LangChain chains
chain = template | model
response = chain.invoke({'domain': 'AWS', 'topic': 'Bedrock'})
print(response.content)
```

## Configuration

- **Model**: GPT-4.1-mini
- **Temperature**: 0.7 (controls randomness in responses)
- **Domain**: AWS (configurable via template variable)
- **Topic**: Bedrock (configurable via template variable)

## Template Structure

The ChatPromptTemplate uses a list of tuples to define the conversation structure:

```python
template = ChatPromptTemplate([
    ('system', 'You are a {domain} expert'),    # System role with domain variable
    ('human', "Tell me about {topic}")          # Human role with topic variable
])
```

### Role Types:
- **System**: Sets the AI's role and behavior
- **Human**: Represents user input
- **AI**: Represents AI responses (not used in this example)

## Pros and Cons

### ✅ **Pros**

#### 1. **Structured Prompting**
- **Role-based Design**: Clear separation between system instructions and user input
- **Template Variables**: Easy parameterization with `{domain}` and `{topic}`
- **Reusable Templates**: Can be used with different domains and topics
- **Professional Structure**: Follows best practices for prompt engineering

#### 2. **LangChain Integration**
- **Chain Pattern**: Clean, readable code using the `|` operator
- **Streamlined Execution**: Combines template and model in one line
- **Framework Benefits**: Leverages LangChain's built-in optimizations
- **Consistent API**: Uses standard LangChain patterns

#### 3. **Flexibility**
- **Dynamic Content**: Easy to change domain and topic without code modification
- **Extensible**: Can easily add more roles or variables
- **Configurable**: Model and temperature can be easily adjusted
- **Modular**: Template and model are separate, allowing easy swapping

#### 4. **Code Quality**
- **Clean Structure**: Well-organized and readable code
- **Best Practices**: Follows LangChain conventions
- **Maintainable**: Easy to modify and extend
- **Documentation**: Clear variable names and structure

### ❌ **Cons**

#### 1. **Limited Functionality**
- **Single Use**: Only demonstrates one prompt execution
- **No Interaction**: No user input or conversation loop
- **Static Example**: Hard-coded domain and topic values
- **No Error Handling**: No protection against API failures

#### 2. **Missing Features**
- **No Conversation Memory**: Doesn't maintain context across interactions
- **No User Interface**: No interactive way to change parameters
- **No Validation**: No input validation or error handling
- **No Persistence**: No saving or loading of templates

#### 3. **Development Limitations**
- **Commented Code**: Contains unused code that should be cleaned up
- **No Examples**: Doesn't show different ways to use the template
- **Limited Documentation**: No inline comments explaining the concepts
- **No Testing**: No examples of different parameter combinations

#### 4. **Production Readiness**
- **No Error Handling**: Will crash on API failures or network issues
- **No Input Sanitization**: Vulnerable to prompt injection attacks
- **No Logging**: No way to track or debug prompt execution
- **No Configuration**: Hard-coded values instead of configurable options

## Example Output

When run, the script will generate a response like:

```
AWS Bedrock is a fully managed service that makes foundation models (FMs) from leading AI companies available through a single API. It provides access to high-performing foundation models from Amazon and other leading AI companies, including AI21 Labs, Anthropic, Cohere, Meta, Stability AI, and Amazon, through a single API.

Key features of AWS Bedrock include:
- Access to multiple foundation models
- Serverless experience for running FMs
- Privacy and security built-in
- Easy integration with AWS services
- Pay-per-use pricing model

Bedrock is particularly useful for building generative AI applications without having to manage the underlying infrastructure...
```

## Usage Examples

### Different Domains and Topics

```python
# Medical expert
response = chain.invoke({'domain': 'Medical', 'topic': 'Diabetes'})

# Programming expert
response = chain.invoke({'domain': 'Programming', 'topic': 'Python'})

# Cooking expert
response = chain.invoke({'domain': 'Cooking', 'topic': 'Italian Cuisine'})
```

### Manual Template Invocation

```python
# Step-by-step approach
prompt = template.invoke({'domain': 'AWS', 'topic': 'Bedrock'})
response = model.invoke(prompt)
print(response.content)
```

## Potential Improvements

1. **Add Error Handling**: Implement try-catch blocks for robust operation
2. **Create Interactive Interface**: Allow users to input domain and topic
3. **Add Input Validation**: Validate and sanitize user inputs
4. **Implement Logging**: Add logging for debugging and monitoring
5. **Create Configuration System**: Make parameters configurable
6. **Add More Examples**: Show different template structures
7. **Implement Conversation Memory**: Add context awareness
8. **Add Template Persistence**: Save and load templates from files

## Dependencies

- `langchain-openai`: LangChain integration with OpenAI
- `langchain-core`: Core LangChain functionality
- `python-dotenv`: Environment variable management

## Related Concepts

- **Prompt Engineering**: Best practices for creating effective prompts
- **Role-based Messaging**: Using different roles in conversation design
- **Template Variables**: Dynamic content injection in prompts
- **LangChain Chains**: Streamlined execution patterns
- **Chat Models**: Specialized models for conversational AI

## License

This project is part of a learning tutorial and is for educational purposes.
