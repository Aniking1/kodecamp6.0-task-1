import os
import sys
import json
import requests
from dotenv import load_dotenv

# Step 1: Load environment configurations from the local hidden .env file
load_dotenv()

# Step 2: Extract variables adhering strictly to the required task names
API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL_NAME")

# Step 3: Enforce strict guard checks to ensure credentials are populated
if not API_KEY or not MODEL:
    print("Error: Missing mandatory environment variables. Please check your .env file.")
    sys.exit(1)


def generate_text(prompt: str) -> str:
    """
    Accepts a user prompt as an argument, performs a direct raw HTTP REST API call 
    to OpenRouter.ai, parses the response JSON object, and extracts the model value text.
    """
    url = "https://openrouter.ai/api/v1/chat/completions"
    
    # Compose raw headers for standard HTTP REST specification 
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:3000",  # Required metadata by OpenRouter ranking pipelines
        "X-Title": "Kodecamp Training 6.0"      # Identifies your local CLI platform instance
    }
    
    # Construct payload mapping matching OpenRouter chat completion requirements
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    
    try:
        # Perform the direct network POST request execution
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        # Catch non-200 HTTP response statuses gracefully
        response.raise_for_status()
        
        # Deserialize JSON response payload directly
        response_data = response.json()
        
        # Navigate the JSON structure payload hierarchy safely to isolate raw text response string
        ai_response = response_data["choices"][0]["message"]["content"]
        return ai_response

    except requests.exceptions.RequestException as e:
        print(f"\n[Network Error]: Direct API request execution failed: {e}")
        sys.exit(1)
    except (KeyError, IndexError):
        print("\n[Parsing Error]: Encountered unmappable structural changes in the API response.")
        sys.exit(1)


if __name__ == "__main__":
    # Step 4: Process CLI commands passed via shell termination slices
    # Slicing from index 1 forward cleanly isolates positional string statements
    cli_args = sys.argv[1:]
    
    # Format split terminal entries into a single cohesive phrase
    user_prompt = " ".join(cli_args)
    
    # Fallback user prompt check mechanism
    if not user_prompt:
        print("Usage Configuration Error!")
        print('Execute Command Structure: python main.py "<Insert your query text context here>"')
        sys.exit(1)
        
    print(f"Direct API call sent. Querying target model: '{MODEL}' via OpenRouter...\n")
    
    # Execute the text retrieval function block
    llm_output = generate_text(user_prompt)
    
    # Output cleanly retrieved text data directly to terminal interface
    print("--- LLM Response Output ---")
    print(llm_output)