'''This program will take a review as an input to llm and then take out
summary and sentiments from that as structured output'''

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv();

## Step 1 : Create model

model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.7);

## Step2 : Create Schema

class Review(TypedDict):

    summary: str;
    sentiment: str;

## Step3 : Create with structured model and pass the type of data we want

structured_model = model.with_structured_output(Review);

## Step4 : Invoke pass the review as prompt of the model

result = structured_model.invoke('''
The Starfire X is an absolute powerhouse! The camera is breathtaking, capturing every detail even in low light. Battery life is fantastic; I easily get two full days. It's a bit pricey, but for this level of performance, it's totally worth the investment.
''')

print(result);