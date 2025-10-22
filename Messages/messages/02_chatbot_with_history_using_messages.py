from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from dotenv import load_dotenv

load_dotenv();

model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.7);

messages = [
    SystemMessage(content=f"You are an AI expert")
];

while True:

    user_qeuery = input("You : ");
    messages.append(HumanMessage(content=user_qeuery));

    if user_qeuery == "exit" or user_qeuery == "bye":
        break;
    
    result = model.invoke(messages);
    print(f"AI : {result.content}");
    messages.append(AIMessage(content=result.content));


