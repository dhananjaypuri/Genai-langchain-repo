from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = OpenAI(model="gpt-4.1-nano");

result = llm.invoke("What is the capital of India?");

print(result);