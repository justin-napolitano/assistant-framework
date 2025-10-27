import os, asyncio
from dataclasses import dataclass
from langchain_openai import ChatOpenAI
from langchain.agents import Tool, initialize_agent, AgentType

# New: use the client + tool
from services.weather_client import weather_today
from tools.weather_tool import weather_tool

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

def _parse_city_state(s: str):
    """
    Accepts:
      "/weather Orlando, FL"  -> ("Orlando", "FL")
      "/weather Orlando"      -> ("Orlando", None)
      "Orlando, FL"           -> ("Orlando", "FL")
      "Orlando"               -> ("Orlando", None)
    """
    if not s:
        return None, None
    q = s.replace("/weather", "").strip().strip(",")
    if "," in q:
        c, st = [x.strip() for x in q.split(",", 1)]
        return (c or None, st or None)
    parts = q.split()
    if len(parts) >= 2:
        return (" ".join(parts[:-1]).strip() or None, parts[-1].strip() or None)
    return (q or None, None)

@dataclass
class AssistantAgent:
    agent: any

    async def run(self, sender: str, text: str) -> str:
        t = text.strip()

        # /weather (direct call to service client; fast and predictable)
        if t.startswith("/weather"):
            city, state = _parse_city_state(t)
            if not city:
                city = os.getenv("WEATHER_DEFAULT_CITY", os.getenv("DEFAULT_CITY", "Orlando"))
            if not state:
                state = os.getenv("WEATHER_DEFAULT_STATE", None)
            return await asyncio.to_thread(weather_today, city, state)

        # /run <cmd>
        if t.startswith("/run "):
            cmd = t[len("/run "):].strip()
            out = await asyncio.to_thread(run_safe, cmd)
            return f"```\n{out}\n```" if out else "(no output)"

        # /ask <q> (RAG)
        if t.startswith("/ask ") and query_docs:
            q = t[len("/ask "):].strip()
            ans = await asyncio.to_thread(query_docs, q)
            return ans

        # Fallback to LLM agent w/ tools (includes weather_tool for NL queries)
        if self.agent:
            return await asyncio.to_thread(self.agent.run, text)

        return "LLM not configured. Try /weather, /run <cmd>, or set OPENAI_API_KEY."

def get_agent(disable_rag: bool = True) -> AssistantAgent:
    tools = [
        # Keep shell as a simple Tool
        Tool(name="run", func=run_safe, description="Run whitelisted shell commands"),
        # Add weather StructuredTool so the LLM can call it in natural language
        weather_tool,
    ]
    try:
        if not disable_rag and 'query_docs' in globals() and query_docs:
            tools.append(Tool(name="docs", func=query_docs, description="Query local documents"))
    except Exception:
        pass

    if OPENAI_API_KEY:
        llm = ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            api_key=OPENAI_API_KEY,
            temperature=0.2,
        )
        agent = initialize_agent(
            tools,
            llm,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False,
        )
    else:
        class Dummy:
            def run(self, text):
                return ("LLM not configured. Try /weather, /run <cmd>, "
                        "or set OPENAI_API_KEY to enable natural language.")
        agent = Dummy()

    return AssistantAgent(agent)
