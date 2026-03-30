import requests

URL = "http://localhost:8080/inquiry"

print("--- HHaiS Socratic Engine v3 (Interactive Portal) ---")
print("Instructions: Type 'PAL: [your question]' for fast answers.")
print("Type 'exit' to quit.\n")

while True:
    # This line keeps the program open and waiting for YOU
    user_input = input("You (Human Heart): ")
    
    if user_input.lower() in ['exit', 'quit']:
        print("Closing Portal...")
        break

    try:
        response = requests.post(URL, json={"user_input": user_input})
        if response.status_code == 200:
            data = response.json()
            print("\n--- The Logic Path ---")
            for msg in data.get("messages", []):
                print(f"- {msg}")
            print("-" * 30 + "\n")
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Connection Error: Is main.py running in Terminal 1?")
