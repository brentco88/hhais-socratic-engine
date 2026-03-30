# HHaiS Socratic Engine v1
**Architecture:** Multi-Agent State Machine (LangGraph + FastAPI)  
**Philosophy:** Human Heart AI (HHaiS) - Balancing logic with empathy.

## The Challenge
Autonomous agents often enter "infinite loops" or "logic thrashing" when faced with complex philosophical paradoxes, leading to high token costs and system instability.

## The Solution: The Socratic Circuit Breaker
This engine implements a **deterministic state machine** that forces a dialectic tension between:
- **Greek Agent:** Logical Refutation & First Principles.
- **Japanese Agent:** Contextual Awareness & Interdependency.
- **Sanskrit Agent (The Firewall):** Monitors the "Logic Path" and forces a conclusion if the state exceeds 4 iterations.

## Tech Stack
- **LangGraph:** Orchestrating the cyclical agent flow.
- **FastAPI:** Serving the engine as a high-speed API.
- **LangSmith:** Full observability and telemetry.

## Proof of Logic (Live Trace)
https://smith.langchain.com/public/134c715b-c844-494c-9468-0f67cda4510a/r

---
## v2.0 Update: Persistent Memory & State Management
The Socratic Engine now features a **Persistent State Machine** using LangGraph's `MemorySaver`. 

### Key Innovations:
- **Thread-Based Persistence:** Each conversation is assigned a unique `thread_id`, allowing the Greek and Japanese agents to "remember" previous logic paths and reference them in follow-up inquiries.
- **State Reducer Architecture:** Implemented `Annotated` state with `operator.add` to ensure a non-destructive message history (Append-only logic).
- **Deterministic Loop Control:** Added a synchronized `step_count` scoreboard that triggers the Sanskrit Firewall after 3 rounds of dialectic tension, ensuring 100% protection against infinite recursive loops.

### Technical Achievements:
- Resolved "Agentic Amnesia" by maintaining a shared state across multiple API calls.
- Optimized cost-governance by enforcing a hard-stop boundary on autonomous agent cycles.
---

## ### The HHaiS Master Prompt Philosophy: Intentional Friction

In a 2026 landscape dominated by "Vending Machine" AI—where speed is prioritized over substance—**HHaiS (Human Heart AI)** takes a different path. We believe that high-stakes leadership requires **Intentional Friction.**

### The "Cognitive Gearbox"
The HHaiS Master Prompt is architected as a dual-mode system, allowing the user to choose their logical "gear":

1. **Strategic Mode (The Socratic Probe):**
   - **Default State:** All queries are subjected to a three-agent dialectic (Greek, Japanese, and Sanskrit).
   - **Purpose:** To drive human curiosity, challenge cognitive biases, and ensure that "Efficiency" never comes at the cost of "Empathy."
   - **Governance:** A deterministic "Sanskrit Firewall" prevents logic-thrashing and enforces conclusion.

2. **Tactical Mode (The PAL Bypass):**
   - **Trigger:** Prefixing a query with `PAL:` (Prompt-Action-Logic).
   - **Purpose:** For low-stakes, high-velocity execution where immediate answers are required.
   - **Design:** Bypasses the heuristic debate layer for a direct, empathetic summary.

> **"We don't build AI that thinks for you; we build AI that thinks *with* you."**

---
