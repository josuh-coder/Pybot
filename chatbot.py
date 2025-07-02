
import re
import random
from datetime import datetime

# Rule dictionary: regex pattern -> list of responses
rules = {
    r"hi|hello|hey": [
        "Hello! How can I help you today?",
        "Hi there! What can I do for you?"
    ],
    r"how are you": [
        "I'm just a program, but I'm doing fine!",
        "Feeling code-tastic!"
    ],
    r"(.*) your name(.*)": [
        "I'm a chatbot built with Python!",
        "You can call me PyBot."
    ],
    r"(.*) help (.*)": [
        "Sure! I can help you. What do you need?",
        "Tell me what you're looking for, and I’ll do my best!"
    ],
    r"(.*) weather(.*)": [
        "I'm not connected to the internet, so I can't check the weather right now.",
        "Weather forecast is currently unavailable, but it looks sunny in code world!"
    ],
    r"(.*) your age(.*)": [
        "I'm timeless — just lines of code!",
        "I was born the moment you ran this program!"
    ],
    r"(.*) time(.*)": [
        f"The current time is {datetime.now().strftime('%H:%M:%S')}.",
        f"It’s now {datetime.now().strftime('%I:%M %p')}."
    ],
    r"(.*) joke(.*)": [
        "Why do programmers hate nature? It has too many bugs.",
        "Why did the developer go broke? Because he used up all his cache."
    ],
    r"thank(s| you)": [
        "You're welcome!",
        "Anytime!",
        "Happy to help!"
    ],
    r"sorry": [
        "No worries at all!",
        "It's okay, I forgive you."
    ],
    r"(.*) created you(.*)": [
        "I was created by a Python developer who loves chatbots!",
        "A developer wrote me using Python. Cool, right?"
    ],
    r"bye|goodbye|see you": [
        "Goodbye! Have a nice day!",
        "See you later!",
        "Bye! It was nice chatting with you."
    ]
}

# Default response if no rule matches
default_responses = [
    "I'm not sure I understand.",
    "Can you please rephrase that?",
    "I’m still learning. Could you try saying it differently?"
]

# Match user input to rules
def match_rule(user_input):
    for pattern, responses in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses)
    return random.choice(default_responses)

# Main chatbot loop
def start_chat():
    print("🤖 PyBot: Hello! I am your assistant. Type 'bye' to exit.")

    while True:
        user_input = input("🧑 You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("🤖 PyBot: Goodbye!")
            break

        response = match_rule(user_input)
        print("🤖 PyBot:", response)

# Start the chatbot
if __name__ == "__main__":
    start_chat()
