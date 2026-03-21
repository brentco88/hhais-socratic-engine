from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from langgraph.graph import StateGraph, END
import uvicorn

# 1. Logic State
class SocraticState(dict):
    messages: List[str]
    step_count: int

# 2. Agent Nodes
def greek_agent(state):
    print("--- GREEK: Challenging Logic ---")
    state["messages"].append("Greek Agent: Does this premise hold under pressure?")
    state["step_count"] += 1
    return state

def japanese_agent(state):
    print("--- JAPANESE: Evaluating Context ---")
    state["messages"].append("Japanese Agent: How does this fit the unspoken environment?")
    state["step_count"] += 1
    return state

def sanskrit_firewall(state):
    print("--- SANSKRIT: Closing Logic ---")
    state["messages"].append("Sanskrit Agent: The logical theorem is now complete.")
    return state

# 3. Deterministic Router
def socratic_router(state):
    if state["step_count"] >= 3:
        return "firewall"
    return "continue"

# 4. Build Graph
workflow = StateGraph(SocraticState)
workflow.add_node("greek", greek_agent)
workflow.add_node("japanese", japanese_agent)
workflow.add_node("sanskrit", sanskrit_firewall)
workflow.set_entry_point("greek")
workflow.add_edge("greek", "japanese")
workflow.add_conditional_edges("japanese", socratic_router, {"continue": "greek", "firewall": "sanskrit"})
workflow.add_edge("sanskrit", END)
app_engine = workflow.compile()

# 5. API Layer
app = FastAPI()

class Query(BaseModel):
    user_input: str

@app.post("/inquiry")
async def run_inquiry(query: Query):
    initial_state = {"messages": [query.user_input], "step_count": 0}
    final_output = app_engine.invoke(initial_state)
    return final_output

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
