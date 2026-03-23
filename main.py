from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Annotated, Union
import operator
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver 
import uvicorn
import os

# 1. Logic State - THE KEY FIX IS HERE
class SocraticState(dict):
    # This tells LangGraph: "Don't replace the list, ADD to it"
    messages: Annotated[list, operator.add] 
    # This tells LangGraph: "Don't replace the number, ADD to it"
    step_count: Annotated[int, operator.add] 

# 2. Agent Nodes - THEY MUST RETURN DICTIONARIES
def greek_agent(state):
    print("--- GREEK: Challenging Logic ---")
    return {"messages": ["Greek Agent: Does this premise hold?"], "step_count": 1}

def japanese_agent(state):
    print("--- JAPANESE: Evaluating Context ---")
    return {"messages": ["Japanese Agent: What about the environment?"], "step_count": 1}

def sanskrit_firewall(state):
    print("--- SANSKRIT: Closing Logic ---")
    return {"messages": ["Sanskrit Agent: The debate is concluded."], "step_count": 0}

# 3. Deterministic Router
def socratic_router(state):

    if state["step_count"] >= 3:
        return "firewall"
    return "continue"

# 4. Build Graph (The "Engine Room")
workflow = StateGraph(SocraticState)

workflow.add_node("greek", greek_agent)
workflow.add_node("japanese", japanese_agent)
workflow.add_node("sanskrit", sanskrit_firewall)

workflow.set_entry_point("greek")
workflow.add_edge("greek", "japanese")
workflow.add_conditional_edges(
    "japanese", 
    socratic_router, 
    {"continue": "greek", "firewall": "sanskrit"}
)
workflow.add_edge("sanskrit", END)

# NEW: The Memory Checkpointer
memory = MemorySaver()
app_engine = workflow.compile(checkpointer=memory)

# 5. API Layer (The "Front Desk")
app = FastAPI()

class Query(BaseModel):
    user_input: str

@app.post("/inquiry")
async def run_inquiry(query: Query):
    # Every time you use this thread_id, the agents "remember" you
    config = {"configurable": {"thread_id": "brenton_session_1"}}
    
    # We send the user input as a list to match our 'operator.add' state
    initial_state = {"messages": [query.user_input], "step_count": 0}
    
    final_output = app_engine.invoke(initial_state, config=config)
    return final_output

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
