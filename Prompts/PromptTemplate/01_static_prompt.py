from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.7);

st.header("Research Tool");
user_input = st.text_input("Enter your prompt");

if st.button("Summarize"):
    response = model.invoke(user_input);
    st.write(response.content);
