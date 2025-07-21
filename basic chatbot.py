def chatbot():
    print(" ChatBot: Hello! Type something to begin. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi"]:
            print(" ChatBot: Hi there!")
        elif user_input in ["how are you", "how are you doing"]:
            print(" ChatBot: I'm doing great, thank you!")
        elif user_input in ["what is your name"]:
            print(" ChatBot: I'm CodeAlphaBot!")
        elif user_input in ["bye", "exit"]:
            print(" ChatBot: Goodbye! Have a great day!")
            break
        else:
            print("h ChatBot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
