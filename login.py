print("Please enter a username and password")
username = input("Username:")
password = input("Password:")

def login(username, password):
    if 1: #if username, password combo is in database
        print("return account type")
    else:
        print("invalid username or password")

login(username, password)