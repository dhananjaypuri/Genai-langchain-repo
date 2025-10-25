from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from dotenv import load_dotenv

load_dotenv();

model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.7);

messages = [
    SystemMessage(content="You are a Devops expert"),
    HumanMessage(content="What is terraform "),
];

response = model.invoke(messages);
print(response.content);
print(messages.append(AIMessage(content=response.content)));

print(messages);