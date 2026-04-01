import ollama
import sys

def run_persona(model_name, prompt):
    """Hits the local Ollama bridge for a specific persona."""
    response = ollama.chat(model=model_name, messages=[
        {'role': 'user', 'content': prompt}
    ])
    return response['message']['content']

def main():
    print("--- HHaiS SOVEREIGN ENGINE v4 (Gemma 3 4B Powered) ---")
    user_input = input("\nEnter your premise or dilemma: ")
    
    # STEP 1: The Greek Fire (Critique)
    print("\n[STEP 1] Summoning Greek Agent for logical audit...")
    greek_out = run_persona('greek-agent', user_input)
    print(f"\nGREEK CRITIQUE: {greek_out}")
    
    # STEP 2: The Japanese Water (Context)
    print("\n[STEP 2] Summoning Japanese Agent for contextual weaving...")
    japanese_out = run_persona('japanese-agent', greek_out)
    print(f"\nJAPANESE CONTEXT: {japanese_out}")
    
    # --- THE GOVERNANCE GATE ---
    print("\n" + "="*50)
    print("GOVERNANCE PAUSE: Human Heart Signature Required")
    print("="*50)
    
    approval = input("\nType 'Proceed' to synthesize the Sovereign Directive: ")
    
    if approval.lower() == 'proceed':
        # STEP 3: The Sanskrit Ether (Synthesis)
        print("\n[STEP 3] Summoning Sanskrit Agent for final synthesis...")
        sanskrit_out = run_persona('sanskrit-agent', japanese_out)
        print(f"\n[SOVEREIGN DIRECTIVE]:\n{sanskrit_out}")
    else:
        print("\n[ALERT] Logic loop halted by Human Governance. Directive denied.")

if __name__ == "__main__":
    main()
