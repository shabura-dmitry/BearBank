from fileloading import load_file
from datetime import date
#Project Name: Bear Bank
#Team: Dmitry Shabura - ds227s@missouristate.edu
#      Myca Defoore - mgd4s@missouristate.edu
#      Katherine Austin - katherine117@live.missouristate.edu
# Fall 2023
data = load_file()
valid = False
def log_in():
    print("Please enter a username and password")
    username = input("Username:")
    password = input("Password:")
    for i in data:
        if data[i]['username'] == username and data[i]['password'] == password:
            global valid
            valid = True
            print("Login successful")
            print("Last login: " + data[i]['last_login'] + "\n")
            data[i]['last_login'] = str(date.today())
            return data[i]

        else:
            valid = False
        
    if valid == False:
        print("Invalid username or password\n")

def get_valid():
    return valid