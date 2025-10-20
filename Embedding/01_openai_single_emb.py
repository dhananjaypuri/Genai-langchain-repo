from langchain_openai import OpenAIEmbeddings , ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0.7);

result = llm.invoke("What is the capital of india ?");

print(result.content);

embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32);
vector = embedding.embed_query(result.content);     ## This function will embed a single line

print(str(vector));