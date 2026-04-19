# HHaiS Sovereign Engine v5.2
## Multi-Intelligence Model Pipeline (M.I.M.P.) for Edge Governance

HHaiS is a deterministic state machine designed to move AI from "Generative Chat" to **Sovereign Logic**. It utilizes a council of specialized Small Language Models (SLMs) to perform a multi-stage Socratic audit on high-stakes premises.

---

### 🧠 The Cognitive Nodes (Visualizing the Purpose)

To ensure unbiased reasoning, each "node" represents a distinct philosophical filter. This prevents "AI echo chambers" by forcing the logic through different cultural lenses:

1. **Agent A: The Greek Auditor (Logic)**
   * **Model:** DeepSeek-R1 (1.5B)
   * **Purpose:** Acts as the "Prosecutor." It uses Socratic friction to identify logical fallacies, contradictions, and weak points in the user's initial premise.
2. **Agent B: The Japanese Weaver (Context)**
   * **Model:** Sea Lion / Mistral
   * **Purpose:** Acts as the "Architect." It focuses on *Wa* (Harmony), analyzing how the logic affects the broader community and environmental context.
3. **Agent C: The Sanskrit Governor (Ethics)**
   * **Model:** DeepSeek-R1 (1.5B)
   * **Purpose:** Acts as the "Judge." It weighs the logic (Greek) against the context (Japanese) to find *Dharma* (Duty)—the balanced ethical path forward.
4. **Agent D: The Polish Compiler (Execution)**
   * **Model:** Groq LPU (Llama-3.1-8B)
   * **Purpose:** Acts as the "Clerk." It takes the abstract debate and compiles it into a final, deterministic, and actionable directive.

* **Tactical Mode (PAL Bypass):** Triggered by prefixing a query with `PAL:`. Bypasses the debate layer for immediate execution via the Precision Layer.

🧬 Evolution of Logic (Telemetry)
v5.1April 15, 2026Logic DriftTelemetry established. Identified RAM OOM issues. https://smith.langchain.com/public/ea5fdabc-1b9b-4b97-9dab-97b1cf36d8bd/r
v5.2April 16, 2026OperationalImplemented RAM-Relief. v5.2 Gold Run https://smith.langchain.com/public/7d085db9-f02b-4142-8861-cccb0a653b8c/r
> **Engineering Note:** The v5.2 cycle prioritizes data integrity over UI stability. On 8GB RAM edge hardware, the system successfully transmits full telemetry to LangSmith before the host OS triggers an OOM (Out of Memory) process termination. 
---

### 🛠️ Setup & Installation

**1. Prerequisites**
* Python 3.10+
* [Ollama](https://ollama.com/) installed and running.

**2. Clone & Environment**
```bash
git clone [https://github.com/YOUR_USERNAME/hhais_engine.git](https://github.com/YOUR_USERNAME/hhais_engine.git)
cd hhais_engine
python3 -m venv venv
source venv/bin/activate
pip install langchain-ollama langchain-groq


---

### 🚀 Potential Applications
HHaiS is a **Generalized Consensus Framework** applicable to any high-stakes industry:
* **Cyber-Sentinel:** Auditing code vulnerabilities vs. defensive protocols.
* **Medical Jury:** Specialist vs. Generalist audits for diagnostic safety.
* **Trust & Safety:** Policy vs. Cultural Context vs. Freedom of Expression.

*"We don't build AI that thinks for you; we build AI that thinks with you."*
