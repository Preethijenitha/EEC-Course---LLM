from  dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableLambda

prompt_template=ChatPromptTemplate.from_messages({
    ("system","you are a helpful assistant"),
    ("human","{input}")
})
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0)
str_parser=StrOutputParser()
def dictionary_maker(text:str)->dict:
    return {"text":text}

dictionary_maker_runnable=RunnableLambda(dictionary_maker)
prompt_post=ChatPromptTemplate.from_messages({
    ("system","you are a social media post generator"),
    ("human","create a post for the following text for LinkedIn:{text}")
})
chain_link=prompt_post|llm|str_parser
prompt_insta=ChatPromptTemplate.from_messages({
    ("system","you are a social media post generator"),
    ("human","create a post for instagram post:{text}")
})
insta_chain=prompt_insta|llm|str_parser
final_chain=prompt_template|llm|str_parser|dictionary_maker_runnable|RunnableParallel(branches={"linkedIn":chain_link,"Instagram":insta_chain})
response=final_chain.invoke({"input":"What is the capital of france"})
print(response)