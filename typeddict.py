from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

class LlmSchema(TypedDict):
    setup: str
    punchline: str
obj = LlmSchema(
    somesetup="hello",
    punchline="some punchline"
)

print(obj)
