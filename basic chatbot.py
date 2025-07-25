import datetime
import random

def get_response(user_input):
    user_input = user_input.lower()

    # Predefined responses
    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! 👋"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm doing great, thank you! 😊"
    elif user_input in ["what is your name", "who are you"]:
        return "I'm CodeAlphaBot, your Python chatbot assistant!"
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day! 👋"
    elif "time" in user_input:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}"
    elif "date" in user_input:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        return f"Today's date is {today}"
    elif "joke" in user_input:
        jokes = [
            "Why did the programmer quit his job? Because he didn't get arrays. 😂",
            "What do you call 8 hobbits? A hobbyte! 🤣",
            "I told my computer I needed a break, and it said 'No problem. I’ll go to sleep.' 😴"
        ]
        return random.choice(jokes)
    elif "thank" in user_input:
        return "You're welcome! 😊"
    else:
        return "Sorry, I don't understand that yet. Try asking something else!"

def chatbot():
    print("🤖 ChatBot: Hello! Type something to begin. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)

        print("🤖 ChatBot:", response)

        if user_input.lower() in ["bye", "exit", "quit"]:
            break

# Run the chatbot
chatbot()
