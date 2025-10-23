import os, asyncio
from dataclasses import dataclass
from langchain_openai import ChatOpenAI
from langchain.agents import Tool, initialize_agent
from tools.weather import get_weather
from tools.shell import run_safe

try:
    DISABLE_RAG = os.getenv("DISABLE_RAG", "true").lower() in ("1","true","yes")
    if not DISABLE_RAG:
        from rag.indexer import query_docs
    else:
        query_docs = None
except Exception:
    query_docs = None
    DISABLE_RAG = True

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class ToolError(Exception): pass

@dataclass
class AssistantAgent:
    agent: any

    async def run(self, sender: str, text: str) -> str:
        if text.startswith("/weather"):
            parts = text.split(maxsplit=1)
            city = parts[1].strip() if len(parts) > 1 else os.getenv("DEFAULT_CITY","Orlando")
            return await asyncio.to_thread(get_weather, city)

        if text.startswith("/run "):
            cmd = text[len("/run "):].strip()
            out = await asyncio.to_thread(run_safe, cmd)
            return f"```\n{out}\n```" if out else "(no output)"

        if text.startswith("/ask ") and query_docs:
            q = text[len("/ask "):].strip()
            ans = await asyncio.to_thread(query_docs, q)
            return ans

        if self.agent:
            return await asyncio.to_thread(self.agent.run, text)
        return "LLM not configured. Try /weather, /run <cmd>, or set OPENAI_API_KEY."

def get_agent(disable_rag: bool = True) -> AssistantAgent:
    tools = [
        Tool(name="weather", func=get_weather, description="Get weather for a city like 'Orlando'"),
        Tool(name="run", func=run_safe, description="Run whitelisted shell commands"),
    ]
    try:
        if not disable_rag and 'query_docs' in globals() and query_docs:
            tools.append(Tool(name="docs", func=query_docs, description="Query local documents"))
    except Exception:
        pass

    if OPENAI_API_KEY:
        llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL","gpt-4o-mini"),
                         api_key=OPENAI_API_KEY,
                         temperature=0.2)
        agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description", verbose=False)
    else:
        class Dummy:
            def run(self, text):
                return ("LLM not configured. Try /weather, /run <cmd>, "
                        "or set OPENAI_API_KEY to enable natural language.")
        agent = Dummy()

    return AssistantAgent(agent)
