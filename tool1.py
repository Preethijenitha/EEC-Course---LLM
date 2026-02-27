from pydantic.v1.fields import FieldInfo as FieldInfoV1

from langchain_community.tools import DuckDuckGoSearchRun


search = DuckDuckGoSearchRun()

result=search.invoke("who is Shahjahan ?")
print(result)