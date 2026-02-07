from dotenv import load_dotenv
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

text = ["My name is Dhananjay Puri and I am a devops engineer ."];

embedding = OpenAIEmbeddings();

vector_db = FAISS.from_texts(text, embedding=embedding); ## Text always takes a list

query = "What is my name";

result = vector_db.similarity_search(query=query,k=2);

for r in result:
    print("-", r.page_content);
