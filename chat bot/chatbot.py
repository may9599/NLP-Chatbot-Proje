import json
import random

with open("intents.json", "r") as file:
    data = json.load(file)

print("AI Chatbot Started! Type quit to stop")

while True:
    user = input("You: ")

    if user.lower() == "quit":
        print("Bot: Goodbye!")
        break

    found = False

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if user.lower() == pattern.lower():
                print("Bot:", random.choice(intent["responses"]))
                found = True

    if not found:
        print("Bot: Sorry, I didn't understand that.")