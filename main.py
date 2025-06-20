from chatbot import ask_chatgpt

def main():
    print("🤖 Welcome to Groq Chatbot CLI!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("👋 Goodbye!")
            break

        response = ask_chatgpt(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
