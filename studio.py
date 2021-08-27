import json
import pickle
print("TommyChatbot Studio")
print("Welcome!")
print("This program makes TommyChatbot Framework files.")
print("To run the files created, you need to configure framework.py.")
print("Now, what do you want it to be named?")
print("(yourname).std")
name = input("Enter in file name: ")
print("Creating file...")
file = open(f"{name}.std", "a")
print("Created file " + name + ".std")
print("OK!")
print("First, do you want to encode with JSON or Pickle?")
print("JSON is easier to edit, but more secure, and compatible with all TommyChatbot engines.")
print("Pickle is harder to edit, but you are comprimising editability for security.")
print("Pickle is only compatible with Python-based engines.")
print("Choose Pickle if you want an insecure, uneditable, file,")
print("And choose JSON for compatibilty, security, but editablity.")
format = input("You: ")
if "JSON" in format:
    print("Creating JSON project.")
    format = "json"
else:
    print("Creating Pickle project.")
    format = "pickle"
print("Now, do you want to let the user choose the name, or choose one name for all users?")
data = {}
data['chatbotnamep'] = input("You: ")
if "User" in data['chatbotnamep'] or "user" in data['chatbotnamep']:
    print("The user will choose the name when they run this file.")
else:
    print("You get to choose the name!")
    print("But of course you have to choose the name!")
    data['chatbotname'] = input("Enter in the name: ")
print("Now, do you want your chatbot to have a save file?")
answer = input("You: ")
if "Yes" in answer or "yes" in answer:
    print("OK, but I need to know where that save file is located.")
    data['savefilep'] = "yes"
    print("Now, this will be in (yourname).mem")
    data['savefile'] = input("Name: ")
    print("This save file will be in the format this project is in.")
else:
     data['savefilep'] = "no"
print("Now, let's get to the juicy stuff. The creation.")
if format == "pickle":
    print(b"Your data so far: " + pickle.dumps(data))
    print("Doesn't make any sense, right?")
else:
    print("Your data so far: " + json.dumps(data, separators=(',', ':')))
print("Now, this is REALLY complex.")
print("When you are done, type in the following: ")
print("finishchatbotcoding()")
print("A lot like Python, right?")
print("Hope you have your TommyChatbot Studio manual with you!")
print("(Contained in manual.md)")