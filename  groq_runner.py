from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=1.3)
response=llm.invoke("tell me a riddle")
print(response.content)