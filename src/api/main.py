from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from typing import cast
from langchain_core.runnables import RunnableConfig  # Yeh import add karo

load_dotenv()
from src.core.agent import app as agent_app, AgentState

app = FastAPI()

class AgentRequest(BaseModel):
    task: str

@app.post("/run-agent")
async def run_agent(request: AgentRequest):
    # 1. State cast
    state = cast(AgentState, {"task": request.task, "result": ""})
    
    # 2. Config cast (Ab error nahi aayega)
    config = cast(RunnableConfig, {"configurable": {"thread_id": "test_session"}})
    
    # 3. Invoke
    result = agent_app.invoke(state, config=config)
    
    return {"status": "success", "agent_output": result["result"]}