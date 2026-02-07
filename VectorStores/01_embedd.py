from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv();

text = "I am a DevOps engineer";

embedding = OpenAIEmbeddings();

## Embedding single of multipline text

vector = embedding.embed_query(text=text);

print(type(vector));
print(len(vector));
print(vector[:5]);