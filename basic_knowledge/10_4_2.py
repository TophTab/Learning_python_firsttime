import json

try:
    with open('username.json') as f_obj:
        username=json.load(f_obj)
except FileNotFoundError:
    username=input("What's your name?")
    with open('username.json','w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remember you when you come back, "+username.title()+"!")
else:
    print("Welcome back, "+username.title()+"!")