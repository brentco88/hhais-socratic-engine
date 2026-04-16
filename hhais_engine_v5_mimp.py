import os
import time
from langchain_ollama import OllamaLLM
from langchain_groq import ChatGroq

# Note: LangChain automatically finds your LANGCHAIN_API_KEY and 
# GROQ_API_KEY from your .bashrc. No extra code needed!

def run_persona(model_name, prompt, stage_name, use_groq=False):
    """Orchestrates model calls with stability pauses."""
    print(f"\n[SYSTEM]: Initializing {stage_name}...")
    
    if use_groq:
        # TACTICAL MODE: Use Groq Cloud for RAM relief
        print(f"[RAM-RELIEF]: Routing {stage_name} to Groq LPU...")
        llm = ChatGroq(model="llama-3.1-8b-instant")
    else:
        # SOVEREIGN MODE: Use Local Ollama
        llm = OllamaLLM(model=model_name)
    
    # LangChain's .invoke() automatically sends the trace to LangSmith
    response = llm.invoke(prompt)
    
    # STABILITY: The "Chromebook Breathing Room"
    print(f"[STABILITY]: {stage_name} complete. Flushing memory (2s)...")
    time.sleep(2)
    
    return response

def main():
    print("--- HHaiS SOVEREIGN ENGINE v5.2 (2026 Standard) ---")
    user_input = input("\nEnter your premise or dilemma: ")
    
    # 1. GREEK (Logic) - Local
    greek_out = run_persona('greek-agent', user_input, "Greek Auditor")
    print(f"GREEK: {greek_out}")
    
    # 2. JAPANESE (Context) - Local (Lightweight 3.2GB)
    jap_out = run_persona('japanese-agent', greek_out, "Japanese Weaver")
    print(f"JAPANESE: {jap_out}")
    
    # 3. SANSKRIT (Governor) - Local
    sans_out = run_persona('sanskrit-agent', jap_out, "Sanskrit Governor")
    print(f"SANSKRIT: {sans_out}")

    print("\n" + "="*50 + "\nGOVERNANCE GATE: Polish Precision Required\n" + "="*50)
    
    if input("\nType 'Execute' to finalize the directive: ").lower() == 'execute':
        # 4. POLISH (Executioner) - USES GROQ FOR RAM RELIEF
        # This prevents the final crash that was closing your terminal!
        polish_out = run_persona('', sans_out, "Polish Compiler", use_groq=True)
        print(f"\n[FINAL SOVEREIGN DIRECTIVE]:\n{polish_out}")
    else:
        print("\n[ALERT] Execution halted by Human Governance.")

if __name__ == "__main__":
    main()
