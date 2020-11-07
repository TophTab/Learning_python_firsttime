import json

def get_stored_username():
    try:
        with open('username.json') as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username=input("What's your name?")
    with open('username.json','w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    username=get_stored_username()
    if username:
        print("Welcome back, "+username.title()+"!")
    else:
        username=get_new_username()
        print("We'll remember you when you come back, "+username.title()+"!")

greet_user()



