# ai-chatbot-project
project for OS lec class, using Gemini 2.5 Flash API

# Setup
Clone the repository (either through VSCode source control or using `git clone https://github.com/NeoRedcraft/ai-chatbot-project`)
## Requirements
**run command below to automatically install dependencies.**
    * `pip install -r requirements.txt`
    * Make sure you have **Python 3.10+** installed.

## Gemini API Access Token
Incase something happens to the Access Token, to this:
1. Go to `https://ai.google.dev/gemini-api/docs/api-key`
2. Get a API key via `https://aistudio.google.com/api-keys`
3. Look at the `chatbot_api.py` to know how the `API_KEY` is setted up.

## Folders and Files
`main.py` - main chat loop.
`chatbot_api.py` - api logic and gemini
`requirements.txt` dependencies for pip install