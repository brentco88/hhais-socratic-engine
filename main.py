from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Annotated, Union
import operator
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver 
import uvicorn

# 1. Logic State
class SocraticState(dict):
    messages: Annotated[list, operator.add] 
    step_count: Annotated[int, operator.add] 

# 2. Agent Nodes
def greek_agent(state):
    print("--- MODE: STRATEGIC (GREEK) ---")
    return {"messages": ["Greek Agent: Challenging the logic..."], "step_count": 1}

def japanese_agent(state):
    print("--- MODE: STRATEGIC (JAPANESE) ---")
    return {"messages": ["Japanese Agent: Evaluating context..."], "step_count": 1}

def sanskrit_firewall(state):
    print("--- SANSKRIT: Governance Complete ---")
    return {"messages": ["Sanskrit Agent: Human verdict accepted. Closing logic."], "step_count": 0}

def pal_node(state):
    print("--- MODE: TACTICAL (PAL) ---")
    return {"messages": ["PAL: Efficiency path identified. Ready for execution."], "step_count": 3}

# 3. Gearbox Router (Checks the LATEST intent)
def gearbox_router(state):
    last_message = state["messages"][-1]
    if "PAL:" in last_message.upper():
        return "tactical"
    return "strategic"

def socratic_router(state):
    if state["step_count"] >= 3:
        return "firewall"
    return "continue"

# 4. Build Graph with Interrupt
workflow = StateGraph(SocraticState)
workflow.add_node("greek", greek_agent)
workflow.add_node("japanese", japanese_agent)
workflow.add_node("sanskrit", sanskrit_firewall)
workflow.add_node("pal", pal_node)

workflow.set_conditional_entry_point(gearbox_router, {"tactical": "pal", "strategic": "greek"})
workflow.add_edge("pal", "sanskrit") 
workflow.add_edge("greek", "japanese")
workflow.add_conditional_edges("japanese", socratic_router, {"continue": "greek", "firewall": "sanskrit"})
workflow.add_edge("sanskrit", END)

memory = MemorySaver()
# THIS LINE IS PHASE 51: The engine FREEZES before Sanskrit
app_engine = workflow.compile(
    checkpointer=memory, 
    interrupt_before=["sanskrit"] 
)

# 5. API Layer
app = FastAPI()

class Query(BaseModel):
    user_input: str

@app.post("/inquiry")
async def run_inquiry(query: Query):
    config = {"configurable": {"thread_id": "brenton_v3"}}
    state = app_engine.get_state(config)
    
    if state.next: # Check if the engine is currently "Paused"
        print("--- RESUMING: Human Heart has provided a verdict ---")
        app_engine.invoke(None, config=config) 
    else:
        print("--- STARTING: Initiating new debate ---")
        app_engine.invoke({"messages": [query.user_input], "step_count": 0}, config=config)
    
    final_state = app_engine.get_state(config)
    return {"messages": final_state.values["messages"]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
