from fileloading import load_file
print("Please enter a username and password")
username = input("Username:")
password = input("Password:")
filename = "C:/Users/ds227s/Documents/GitHub/BearBank/user_database.json"
def login(username, password):
    data = load_file()
    for account in range(len(data)):
        if data['username'] == username and data['password'] == password:
            create_menu(data['account_type'])
    else:
        print("invalid username or password")

login(username, password)

def create_menu(account_type):
    if account_type == 0:
        pass
    elif account_type == 1:
        pass
    elif account_type ==2:
        pass
    else:
        print("error")