from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

class LlmSchema(BaseModel):
    setup: str
    punchline: str
obj = LlmSchema(
    setup="some setup",
    punchline="some punchline"
)

print(obj)
