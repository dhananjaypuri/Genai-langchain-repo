from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-nano");

result = llm.invoke("What is the capital of India?");

print(result.content);
