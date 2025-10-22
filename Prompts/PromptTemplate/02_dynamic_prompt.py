from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import streamlit as st
from dotenv import load_dotenv

load_dotenv();

model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.7);

template = '''
You are a holiday planner.
Plan and summarize a trip and itenary for titled place : {destination}.
Traveling in the season of {season} for the given days {days}.
If certain information is not available , respond with: "Insufficient
information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and
length.
''';

st.header("Holiday Planner");
destination = st.text_input("Enter the Destination");
days = int(st.number_input("No of Days"));
season = st.selectbox("Select the season", ["Summers", "Winters", "Monsoon"]);

prompt = PromptTemplate(template=template, input_variables=['destination', 'days', 'season']);

pt = prompt.invoke({
    'destination': destination,
    'days': days,
    'season': season
});

if st.button("Summarize"):
    result = model.invoke(pt);
    st.write(result.content);