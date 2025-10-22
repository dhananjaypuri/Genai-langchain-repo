from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, ChatMessagePromptTemplate
from dotenv import load_dotenv

load_dotenv();

model = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7);

template = ChatPromptTemplate([
    ('system', 'You are a {domain} expert'),
    ('human', "Tell me about {topic}")
]);

# prompt = template.invoke({'domain': 'AWS', 'topic': 'Bedrock'});

# response = model.invoke(prompt);

# print(response.content);

chain = template | model;
response = chain.invoke({'domain': 'AWS', 'topic': 'Bedrock'});
print(response.content);

