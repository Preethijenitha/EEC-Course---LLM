from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0)
from langchain_community.tools import DuckDuckGoSearchRun
search_tool= DuckDuckGoSearchRun(description="this is tool to search the new ")
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
wikipedia_tool= WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(),description="this is a good tool")
from langchain.tools import tool
@tool
def enterprise_tool(query:str)->str:
    """this is a tool to send emails"""
    return "Email send"
Toolkit=[search_tool,wikipedia_tool,enterprise_tool]
from langchain.agents import create_agent
model=ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.1,
    max_tokens=1000,
    timeout=30
)
agent=create_agent(model,tools=Toolkit)
graph=agent.get_graph()
graph.print_ascii()
example_query = "what is the capital of france?"

events = agent.stream(
    {"messages": [("user", example_query)]},
    stream_mode="values",
)
for event in events:
    event["messages"][-1].pretty_print()