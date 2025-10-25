
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st
from dotenv import load_dotenv
import json

load_dotenv();

model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.7);

template = load_prompt("template.json");

st.header("Holiday Planner");
destination = st.text_input("Enter the Destination");
days = int(st.number_input("No of Days"));
season = st.selectbox("Select the season", ["Summers", "Winters", "Monsoon"]);


pt = template.invoke({
    'destination': destination,
    'days': days,
    'season': season
});

if st.button("Summarize"):
    result = model.invoke(pt);
    st.write(result.content);