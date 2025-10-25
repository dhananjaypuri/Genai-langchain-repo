from typing import TypedDict , Annotated, Literal, Optional
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv();

model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.7);

class Review(TypedDict):
    summary: Annotated[str, "A small summary of the review"];
    sentiment: Annotated[Literal["pos", "neg"], "Postive or negative sentiments as per the review"];
    pros: Annotated[Optional[list[str]],"Extract a list of pros only if a section named 'PROS' or 'PRO' is explicitly present. Otherwise, return null or an empty list."];
    cons: Annotated[Optional[list[str]],"Extract a list of cons only if a section named 'CONS' or 'CON' is explicitly present. Otherwise, return null or an empty list."];
    name: Annotated[Optional[str], "This is the name of the author of the review"];

structured_model = model.with_structured_output(Review);

result = structured_model.invoke('''
The Chrono-Drive 7000 is a very expensive, high-end smartwatch built for athletes. It is built like a tank using titanium metal and has a screen that is the brightest available, so you can see it easily in the sun.

The watch is great at health tracking. It measures recovery, fatigue, and other advanced stats very accurately. The battery lasts about 7 to 9 days, which is very good. And when it finally runs out, it can charge to 80% in only 15 minutes.

The main problems are the high price, its large size, and the lack of popular apps.

''');

print(result);

## OUTPUT - There is an issue with the output , its fetching pros , cons and name as its not present in the review, llm is implicitly fecthing details

'''
{'name': 'Chrono-Drive 7000', 'summary': 'A high-end, durable smartwatch tailored for athletes with excellent health tracking and fast charging, but limited app ecosystem and a sizable design.', 'pros': ['Durable titanium build', 'Bright screen visible in sunlight', 'Accurate health metrics (recovery, fatigue, etc.)', 'Long battery life (7-9 days)', 'Fast charging to 80% in 15 minutes'], 'cons': ['High price point', 'Large size may not suit all users', 'Limited selection of popular apps'], 'sentiment': 'pos'}
'''