from fileloading import load_file
print("Please enter a username and password")
username = input("Username:")
password = input("Password:")
filename = "C:/Users/ds227s/Documents/GitHub/BearBank/user_database.json"
def login(username, password):
    data = load_file()
    for account in range(len(data)):
        print(len(data))
    else:
        print("invalid username or password")

login(username, password)