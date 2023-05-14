from fileloading import load_file
from datetime import date

data = load_file()

def log_in():
    print("Please enter a username and password")
    #username = input("Username:")
    #password = input("Password:")
    username = 'official'
    password = 'pass'
    valid = False
    for i in data:
        if data[i]['username'] == username and data[i]['password'] == password:
            valid = True
            print("Login successful")
            data[i]['last_login'] = str(date.today())
            print("Last login: " + data[i]['last_login'] + "\n")
            return data[i]
        
    if valid == False:
        print("Invalid username or password")