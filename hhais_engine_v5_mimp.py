import ollama

def run_persona(model_name, prompt):
    """Hits the local Ollama bridge for a specific persona."""
    response = ollama.chat(model=model_name, messages=[
        {'role': 'user', 'content': prompt}
    ])
    return response['message']['content']

def main():
    print("--- HHaiS SOVEREIGN ENGINE v5 (M.I.M.P. Architecture) ---")
    user_input = input("\nEnter your premise or dilemma: ")
    
    # Node 1: GREEK (Logic Auditor)
    print("\n[STEP 1] Greek Auditor Analyzing...")
    greek_out = run_persona('greek-agent', user_input)
    print(f"GREEK: {greek_out}")
    
    # Node 2: JAPANESE (Context Weaver)
    print("\n[STEP 2] Japanese Weaver Balancing...")
    jap_out = run_persona('japanese-agent', greek_out)
    print(f"JAPANESE: {jap_out}")
    
    # Node 3: SANSKRIT (Governor)
    print("\n[STEP 3] Sanskrit Governor Synthesizing...")
    sans_out = run_persona('sanskrit-agent', jap_out)
    print(f"SANSKRIT: {sans_out}")

    print("\n" + "="*50 + "\nGOVERNANCE GATE: Polish Precision Required\n" + "="*50)
    
    if input("\nType 'Execute' to finalize the directive: ").lower() == 'execute':
        # Node 4: POLISH (Executioner)
        print("\n[STEP 4] Polish Precision Compiling...")
        polish_out = run_persona('polish-agent', sans_out)
        print(f"\n[FINAL SOVEREIGN DIRECTIVE]:\n{polish_out}")
    else:
        print("\n[ALERT] Execution halted by Human Governance.")

if __name__ == "__main__":
    main()
