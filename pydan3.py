from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

class LlmSchema(BaseModel):
    setup: str
    punchline: str
llm_structured_output=llm.with_structured_output(LlmSchema)
response=llm_structured_output.invoke("Tell me a joke")
print(response.setup)

