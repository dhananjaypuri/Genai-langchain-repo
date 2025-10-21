# PromptTemplate Examples

This folder contains examples demonstrating different ways to work with LangChain PromptTemplates, from basic static prompts to dynamic templates and template persistence.

## Files Overview

### 1. `01_static_prompt.py` - Basic Static Prompt
A simple example showing how to use a basic static prompt with a ChatOpenAI model.

**Features:**
- Basic Streamlit interface
- Simple text input for user prompts
- Direct model invocation without template formatting
- Uses GPT-4.1-nano model with temperature 0.7

**Usage:**
```bash
streamlit run 01_static_prompt.py
```

### 2. `02_dynamic_prompt.py` - Dynamic Prompt Template
Demonstrates how to create and use dynamic prompt templates with variable substitution.

**Features:**
- Holiday planner application
- Dynamic prompt template with input variables: `destination`, `days`, `season`
- Streamlit interface with multiple input types:
  - Text input for destination
  - Number input for days
  - Selectbox for season selection
- Template-based prompt generation

**Key Components:**
- `PromptTemplate` with custom template string
- Input variables: `['destination', 'days', 'season']`
- Template includes conditional logic for insufficient information

**Usage:**
```bash
streamlit run 02_dynamic_prompt.py
```

### 3. `03_save_template.py` - Save Template to File
Shows how to save a PromptTemplate to a JSON file for reuse.

**Features:**
- Creates a PromptTemplate with the same holiday planner template
- Saves the template to `template.json` file
- Demonstrates template persistence for reuse across applications

**Template Structure:**
- Input variables: `destination`, `season`, `days`
- Template format: f-string
- Includes validation and metadata options

**Usage:**
```bash
python 03_save_template.py
```

### 4. `04_load_prompt_template.py` - Load Template from File
Demonstrates how to load a previously saved PromptTemplate from a JSON file.

**Features:**
- Loads template from `template.json` using `load_prompt()`
- Same Streamlit interface as dynamic prompt example
- Shows template reuse and persistence
- Identical functionality to `02_dynamic_prompt.py` but with loaded template

**Usage:**
```bash
streamlit run 04_load_prompt_template.py
```

## Template Structure

The saved template (`template.json`) contains:
- **Input Variables**: `destination`, `season`, `days`
- **Template Format**: f-string
- **Purpose**: Holiday planning with seasonal considerations
- **Validation**: Handles insufficient information gracefully

## Dependencies

All examples require:
- `langchain-openai`
- `langchain-core`
- `streamlit`
- `python-dotenv`

Install with:
```bash
pip install langchain-openai langchain-core streamlit python-dotenv
```

## Environment Setup

Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Learning Progression

1. **Static Prompt** → Learn basic model interaction
2. **Dynamic Template** → Understand variable substitution
3. **Save Template** → Learn template persistence
4. **Load Template** → Understand template reuse

This progression demonstrates the evolution from simple prompts to reusable, persistent template systems in LangChain.
