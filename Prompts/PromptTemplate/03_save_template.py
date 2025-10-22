from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

template = '''
You are a holiday planner.
Plan and summarize a trip and itenary for titled place : {destination}.
Traveling in the season of {season} for the given days {days}.
If certain information is not available , respond with: "Insufficient
information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and
length.
''';

prompt = PromptTemplate(template=template, input_variables=["destination", "season", "days"]);

prompt.save("/Users/dhananjaypuri/study/data-science/books-project/mcp-tut/gen-ai/Prompts/PromptTemplate/template.json");