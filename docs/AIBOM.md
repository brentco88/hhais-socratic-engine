# AI Bill of Materials (AIBOM)
**Project:** HHaiS Sovereign Engine v5.2 (M.I.M.P.)
**Objective:** Deterministic Customer Success & Cognitive Governance

## 1. Hardware & Orchestration
* **Target Compute Environment:** NVIDIA Jetson Orin Nano (Edge Local) / 8GB Unified Memory
* **Orchestration Layer:** LangGraph / LangChain Core
* **Telemetry & Tracing:** LangSmith (Configured for PII redaction)

## 2. Model Pipeline (The Council)
* **Agent A (Greek Auditor):** DeepSeek-R1 (1.5B) - *Local*
* **Agent B (Japanese Weaver):** Sea Lion v3 (3B/8B) - *Local*
* **Agent C (Sanskrit Governor):** DeepSeek-R1 (1.5B) - *Local*
* **Agent D (Polish Compiler):** Ministral-3 (3B) / Groq LPU API - *Hybrid*

## 3. Safety Guardrails & Protocols
* **Data Sovereignty:** 100% local inference for logic processing. Zero enterprise PII transmitted to external LLMs.
* **The Frustration Index (FI):** Circuit-breaker logic that halts infinite loops if semantic delta is not achieved within 3 iterations.
* **Agentic Aporia Gateway:** Hard-coded prompt injection prevention that blocks the system from executing without human-in-the-loop Socratic validation.
