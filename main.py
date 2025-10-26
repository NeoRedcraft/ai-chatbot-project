from chatbot_api import get_chatbot_reply

def main():
    print("🤖 Granite Chatbot (Hugging Face API) — type 'exit' to quit.\n")
    conversation = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye 👋")
            break

        reply = get_chatbot_reply(conversation, user_input)
        print(f"Bot: {reply}")


if __name__ == "__main__":
    main()
