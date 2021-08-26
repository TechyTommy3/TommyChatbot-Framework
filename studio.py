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
    print("Creating JSON file.")
    format = "json"
else:
    print("Creating Pickle file.")
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
print("Now, do you want ")