from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

prompt_template=ChatPromptTemplate.from_messages({
    ("system","youa are a heplful assistant"),
    ("human","{input}")
})
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0.3)
str_parser=StrOutputParser()
chain=runnable(prompt_template | llm | str_parser)
response=chain.invoke({"input":"what is capital of Japan"})
print(response)