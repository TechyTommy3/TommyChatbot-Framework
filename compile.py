import pickle
import json
print("Welcome to compileChatbot!")
print("This program allows you to make chatbots that run without framework.py.")
print("This also creates custom .py files for people that have Python installed, and makes your TommyChatbot Web files!")
print("So, what do you want to create?")
answer = input("You: ")
if "Python" in answer:
    print("Creating a Python file!")
elif "Web" in answer or "Website" in answer or "web" in answer or "website" in answer:
    print("Making a copy of TommyChatbot Web!")
else:
    print("Making a standalone program!")