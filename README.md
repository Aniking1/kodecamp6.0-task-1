# Kodecamp 6.0 - AI for Developers (Task 1)

## Project Description
This project demonstrates how to connect to an external Large Language Model (LLM) provider without relying on heavy third-party vendor SDKs. It features a lightweight, single-script Python application that communicates directly with the OpenRouter.ai API using raw HTTP requests.

## Key Features
* **Zero SDK Dependency:** Uses Python's native ecosystem and the standard `requests` library to manage direct endpoint connections.
* **Environment Variable Security:** Implements `python-dotenv` to dynamically handle authentication keys and configuration setups, fully excluding confidential credentials from version control via `.gitignore`.
* **Flexible CLI Interface:** Accepts custom prompts straight from the terminal system arguments (`sys.argv`) and prints clean text outputs back to the console.
* **Smart Fallbacks:** Configured to point dynamically to OpenRouter's free-tier model routing pipeline (`openrouter/free`) for fast, cost-free execution testing.

## Local Setup & Usage

1. **Install Dependencies:**
   ```bash
   pip install requests python-dotenv