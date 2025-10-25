from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv();

model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.7);

while True:

    user_input = input("You : ");
    if user_input == "exit" or user_input == "bye":
        break;
    response = model.invoke(user_input);

    print(f"AI : {response.content}");
