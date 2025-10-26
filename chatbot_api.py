import google.generativeai as genai

API_KEY = "AIzaSyBcZ7nJMHNiwfQgMWoW9O42J3uHLyVDWHs"  # Access Token
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def get_chatbot_reply(conversation_history, user_message):
    conversation = "\n".join(conversation_history + [f"User: {user_message}", "Bot:"])
    try:
        response = model.generate_content(conversation)
        reply = response.text.strip()
    except Exception as e:
        reply = f"(Error: {e})"
    conversation_history.append(f"User: {user_message}")
    conversation_history.append(f"Bot: {reply}")
    return reply
