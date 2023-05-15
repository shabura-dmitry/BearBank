from fileloading import load_file
from datetime import date

data = load_file()

def log_in():
    print("Please enter a username and password")
    username = input("Username:")
    password = input("Password:")
    valid = False
    for i in data:
        if data[i]['username'] == username and data[i]['password'] == password:
            valid = True
            print("Login successful")
            print("Last login: " + data[i]['last_login'] + "\n")
            data[i]['last_login'] = str(date.today())
            return data[i]
        
    if valid == False:
        print("Invalid username or password")