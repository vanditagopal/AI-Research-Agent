from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.exceptions import OutputParserException
from langchain.agents import create_tool_calling_agent, AgentExecutor
from groq import APIError
from langchain.tools import Tool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun
from datetime import datetime
from tools import search_tool,wiki_tool,save_to_txt
import json
import re

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

parser = PydanticOutputParser(pydantic_object=ResearchResponse)


tools = [search_tool, wiki_tool] 

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    streaming=False
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are a helpful research assistant.
        Use the provided tools (search, wikipedia) when needed to gather information.
        After using tools, return the final answer strictly in this JSON format:
        {format_instructions}
        """
    ),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}"),
]).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = input("What can I help you with for research? ")

try:
    raw_response = agent_executor.invoke({"query": query})
    response_text = raw_response.get("output", "")

    try:
        structured_response = parser.parse(response_text)
    except OutputParserException:
        match = re.search(r"\{.*\}", response_text, re.DOTALL)
        if match:
            structured_response = parser.pydantic_object.model_validate_json(match.group())
        else:
            raise OutputParserException("Failed to parse JSON from LLM output.")

    print("\OUTPUT")
    print(f"Topic: {structured_response.topic}")
    print(f"Summary:\n{structured_response.summary}\n")
    print(f"Sources: {', '.join(structured_response.sources)}")
    print(f"Tools Used: {', '.join(structured_response.tools_used)}\n")

    content_to_save = json.dumps(structured_response.model_dump(), indent=2)
    save_result = save_to_txt(content=content_to_save)
    print(save_result)

except APIError as e:
    print("Groq APIError:", e)
    if hasattr(e, "partial_output"):
        print("Partial output:", e.partial_output)
except Exception as e:
    print("Unexpected error:", e)
