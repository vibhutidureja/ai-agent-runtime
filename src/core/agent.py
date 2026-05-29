import os
from pathlib import Path
from dotenv import load_dotenv

# 1. Force Load Environment Variables
dotenv_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=dotenv_path)

# 2. Imports (Yahan se 'ChatGroq' import hona chahiye)
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END
from typing import TypedDict
from src.sandbox.docker_manager import DockerManager
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

# 3. LLM Initialization (Ab 'ChatGroq' defined hai)
llm = ChatGroq(model="llama3-8b-8192")
sandbox = DockerManager()

class AgentState(TypedDict):
    task: str
    result: str

llm = ChatGroq(model="llama-3.3-70b-versatile")
sandbox = DockerManager()

def execute_task(state: AgentState):
    prompt = f"Write only the Python code to: {state['task']}. Do not include markdown or explanations."
    response = llm.invoke(prompt)
    raw_content = getattr(response, 'content', str(response))
    clean_code = str(raw_content).replace("```python", "").replace("```", "").strip()
    output = sandbox.run_code_in_sandbox(clean_code)
    return {"result": output}

# 1. PEHLE Workflow define karo
workflow = StateGraph(AgentState)
workflow.add_node("executor", execute_task)
workflow.set_entry_point("executor")
workflow.add_edge("executor", END)

conn = sqlite3.connect(":memory:", check_same_thread=False)
# 2. PHIR Memory setup karo
memory = SqliteSaver(conn)

# 3. SABSE LAST mein compile karo
app = workflow.compile(checkpointer=memory)