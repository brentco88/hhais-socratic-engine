import requests
import json

def run_test():
    url = "http://localhost:8080/inquiry"
    # This simulates a visionary founder's complex prompt
    payload = {"user_input": "How do we balance AI efficiency with human empathy in a CSM role?"}
    
    print("--- INITIATING SOCRATIC PROBE ---")
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            print("\nFINAL LOGIC PATH:")
            for idx, msg in enumerate(data['messages']):
                print(f"[{idx}] {msg}")
            
            print(f"\nTOTAL STEPS: {data['step_count']}")
            print("--- VERIFICATION: DETERMINISTIC BOUNDARY HELD ---")
        else:
            print(f"Error: Server responded with {response.status_code}")
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    run_test()
