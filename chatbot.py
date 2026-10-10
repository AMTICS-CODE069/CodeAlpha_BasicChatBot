import string
from datetime import datetime


def get_reply(message):
    message = message.lower().translate(str.maketrans("", "", string.punctuation))
    words = message.split()

    if "how are you" in message:
        return "I'm fine, thanks!"
    elif "bye" in words or "goodbye" in words or "exit" in words:
        return "Goodbye!"
    elif "hello" in words or "hi" in words or "hey" in words:
        return "Hi!"
    elif "your name" in message:
        return "I'm PyBot, your simple chatbot!"
    elif "thank" in message:
        return "You're welcome!"
    elif "time" in words:
        return "The time is " + datetime.now().strftime("%I:%M %p")
    elif "help" in words:
        return "Try saying: hello, how are you, what is your name, time, thanks or bye."
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def main():
    print("--- Basic Chatbot ---")
    print("Type 'help' to see what I can do, or 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print("Bot:", reply, "\n")

        if reply == "Goodbye!":
            break


if __name__ == "__main__":
    main()
