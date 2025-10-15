from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from pydantic import BaseModel, Field
from datetime import datetime

def save_to_txt(content: str, filename: str = "research_output.txt") -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{content}\n\n"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    return f"Data  saved to {filename}"


# Web search tool
search_run = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search_run.run,
    description="Search the web for up-to-date information"
)

# Wikipedia tool
wiki_api = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=400)
wiki_tool = Tool(
    name="wikipedia",
    func=wiki_api.run,
    description="Get a summary from Wikipedia for a given topic"
)