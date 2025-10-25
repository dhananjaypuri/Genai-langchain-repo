from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv();

model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.7);
messages = [];
history = [];

while True:

    user_input = input("You : ");
    if user_input == "exit" or user_input == "bye":
        break;
    messages.append(user_input);
    history.append({'user': user_input});
    response = model.invoke(messages);

    print(f"AI : {response.content}");
    messages.append(response.content);
    history.append({'ai': response.content});

print(messages);
print(history);
