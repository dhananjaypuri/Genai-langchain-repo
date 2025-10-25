# 📋 Structured Output with TypedDict

This folder contains examples demonstrating how to use **TypedDict** with LangChain to create structured outputs from Large Language Models (LLMs). These examples show the progression from basic TypedDict usage to advanced structured output techniques.

## 🎯 What You'll Learn

- How to define data structures using TypedDict
- How to extract structured data from LLM responses
- How to handle complex data extraction with proper validation
- How to solve common issues with implicit data extraction

## 📁 Files Overview

| File | Description | Key Features |
|------|-------------|--------------|
| `01_type_dict.py` | Basic TypedDict introduction | Simple data structure definition |
| `02_with_structured_output_typedict.py` | Basic structured output | Review analysis with summary and sentiment |
| `03_with_struc_out_complex_typedict.py` | Complex structured output | Advanced review analysis with pros/cons |
| `04_with_struc_modified.py` | Fixed structured output | Solves implicit extraction issues |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the required dependencies installed:

```bash
pip install langchain-openai python-dotenv
```

### Environment Setup

Create a `.env` file in your project root with your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## 📖 Detailed Examples

### 1. Basic TypedDict (`01_type_dict.py`)

**Purpose**: Introduction to TypedDict for type hints and data structure definition.

```python
from typing import TypedDict

class Student(TypedDict):
    name: str
    marks: float
    age: int

# Usage with type hints
new_student: Student = {"name": "Vijay", "age": 31, "marks": 90}
```

**Key Points**:
- TypedDict provides type hints but **no runtime validation**
- Helps with IDE autocomplete and type checking
- Useful for defining expected data structures

### 2. Basic Structured Output (`02_with_structured_output_typedict.py`)

**Purpose**: Extract structured data from a product review using LLM.

**What it does**:
- Takes a product review as input
- Extracts summary and sentiment
- Returns structured JSON output

**Example Input**:
```
The Starfire X is an absolute powerhouse! The camera is breathtaking, capturing every detail even in low light. Battery life is fantastic; I easily get two full days. It's a bit pricey, but for this level of performance, it's totally worth the investment.
```

**Expected Output**:
```json
{
  "summary": "High-performance smartphone with excellent camera and battery life",
  "sentiment": "pos"
}
```

### 3. Complex Structured Output (`03_with_struc_out_complex_typedict.py`)

**Purpose**: Advanced review analysis with multiple data points.

**Features**:
- Extracts summary, sentiment, pros, cons, and author name
- Uses `Annotated` types for better LLM instructions
- Handles optional fields with `Optional`
- Uses `Literal` for constrained values

**Schema Definition**:
```python
class Review(TypedDict):
    summary: Annotated[str, "A small summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Positive or negative sentiments"]
    pros: Annotated[Optional[list[str]], "List of pros if explicitly present"]
    cons: Annotated[Optional[list[str]], "List of cons if explicitly present"]
    name: Annotated[Optional[str], "Author name if present"]
```

**⚠️ Issue Identified**: This example has a problem where the LLM extracts pros/cons even when they're not explicitly mentioned in the review.

### 4. Fixed Structured Output (`04_with_struc_modified.py`)

**Purpose**: Solves the implicit extraction problem from example 3.

**Key Improvements**:
- **System Message**: Provides clear instructions to the LLM
- **Explicit Rules**: Only extract pros/cons from labeled sections
- **Better Validation**: Prevents implicit data extraction
- **Clear Guidelines**: Defines when to return None vs. actual data

**System Message Rules**:
```
- Do NOT infer or guess pros or cons
- Only extract if section headers like 'Pros:', 'CONS:', etc. exist
- If no section headers, return None
- Do not convert negative sentences into cons
```

---

## 🔧 How to Run

1. **Set up your environment**:
   ```bash
   pip install -r ../../requirement.txt
   ```

2. **Run any example**:
   ```bash
   python 01_type_dict.py
   python 02_with_structured_output_typedict.py
   python 03_with_struc_out_complex_typedict.py
   python 04_with_struc_modified.py
   ```

---

## 🎨 Key Concepts

### TypedDict vs Regular Dict

| Feature | TypedDict | Regular Dict |
|---------|-----------|--------------|
| Type Hints | ✅ Yes | ❌ No |
| Runtime Validation | ❌ No | ❌ No |
| IDE Support | ✅ Excellent | ⚠️ Limited |
| Structure Definition | ✅ Clear | ❌ Unclear |

### LangChain Structured Output

```python
# Basic usage
structured_model = model.with_structured_output(YourTypedDict)

# With messages
result = structured_model.invoke([
    SystemMessage(content="Your instructions"),
    HumanMessage(content="Your input")
])
```

### Best Practices

1. **Use Annotated Types**: Provide clear instructions to the LLM
2. **Handle Optional Fields**: Use `Optional` for fields that might not exist
3. **Provide System Messages**: Give explicit rules to prevent unwanted extraction
4. **Use Literal Types**: Constrain possible values (e.g., sentiment: "pos" or "neg")
5. **Test Edge Cases**: Ensure your schema handles various input formats

---

## 🐛 Common Issues & Solutions

### Issue 1: Implicit Data Extraction
**Problem**: LLM extracts pros/cons even when not explicitly mentioned
**Solution**: Use clear system messages with explicit rules

### Issue 2: Type Validation
**Problem**: TypedDict doesn't validate at runtime
**Solution**: Use Pydantic models for runtime validation (not covered in these examples)

### Issue 3: Optional Fields
**Problem**: LLM returns empty strings instead of None
**Solution**: Use `Optional` types and clear instructions

---

## 🚀 Next Steps

After mastering these examples, consider exploring:

- **Pydantic Models**: For runtime validation
- **Custom Validators**: For complex data validation
- **Streaming Responses**: For real-time structured output
- **Batch Processing**: For multiple structured extractions

---

## 📚 Additional Resources

- [LangChain Structured Output Documentation](https://python.langchain.com/docs/how_to/structured_output)
- [Python TypedDict Documentation](https://docs.python.org/3/library/typing.html#typing.TypedDict)
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)

---

## 🤝 Contributing

Feel free to improve these examples or add new structured output patterns!

