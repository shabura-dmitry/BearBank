import json
print("Please enter a username and password")
username = input("Username:")
password = input("Password:")
filename = "C:/Users/ds227s/Documents/GitHub/BearBank/user_database.json"
def login(username, password):
    for account in account_database():
        print(data)#if username, password combo is in database
        print("return account type")
    else:
        print("invalid username or password")

login(username, password)

def account_database():
    with open(filename) as infile:
        data = json.load(infile)
        return data
        