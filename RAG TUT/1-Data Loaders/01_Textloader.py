from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv();

model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.7);
loader = TextLoader(file_path='music.txt', encoding='utf-8');

prompt = PromptTemplate(template="Summarize the  context : {context} in 2 lines.", input_variables=['context']);

doc = loader.load();
strparser = StrOutputParser();

print(type(doc));
print(len(doc));
print(doc[0].metadata['source']);


context = doc[0].page_content;
context = context.replace("\n", '');

chain = prompt | model | strparser;

print("===================================");
print(chain.invoke({'context': context}));