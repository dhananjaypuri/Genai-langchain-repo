## This problem solves the issue specified on number 3 program
from langchain_openai import ChatOpenAI
from typing import TypedDict , Annotated , Literal , Optional
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

model = ChatOpenAI(model="gpt-4.1-nano", temperature=0.7)

class Review(TypedDict):
    name: Annotated[Optional[str], "Extract the author name only if explicitly present, else None."]
    summary: Annotated[str, "Short summary of the review."]
    pros: Annotated[Optional[list[str]], "Extract ONLY if the text contains a section header: 'Pros:', 'PROS:', or 'Advantages:'. Otherwise return None."]
    cons: Annotated[Optional[list[str]], "Extract ONLY if the text contains a section header: 'Cons:', 'CONS:', or 'Disadvantages:'. Otherwise return None."]
    sentiment: Annotated[Literal["pos", "neg"], "Overall sentiment of the review."]

structured_model = model.with_structured_output(Review)

messages = [
    SystemMessage(
        content=(
"You are extracting structured review data.\n"
        "\n"
        "**SUMMARY RULE:**\n"
        "- Always extract a short summary (1–2 sentences). Never leave summary empty.\n"
        "- The summary must describe the product and overall opinion.\n"
        "\n"
        "**PROS/CONS RULES:**\n"
        "- Do NOT infer or guess pros or cons.\n"
        "- IGNORE any descriptions of problems or praises unless they are inside an explicitly labeled section.\n"
        "- Only extract `pros` if the text contains an exact section header such as 'Pros:', 'PROS:', or 'Advantages:'.\n"
        "- Only extract `cons` if the text contains an exact section header such as 'Cons:', 'CONS:', or 'Disadvantages:'.\n"
        "- If no such section headers exist, return pros=None and cons=None.\n"
        "- Do not convert negative sentences into cons.\n"
        "- Do not convert positive sentences into pros.\n"
        "\n"
        "**NAME RULE:**\n"
        "- Only extract `name` if an author is explicitly named. Otherwise return None."
        )
    ),
    HumanMessage(
        content="""
The Aura 5G feels cheap and plastic. After just a month, the side button has become sticky, and the fingerprint sensor only works half the time. Completely unreliable hardware. I expected much better build quality for the price.
"""
    )
]

result = structured_model.invoke(messages)

print(result)
