import json
from account import open_account
from fileloading import *

data=load_file()

def open_official(logged_in_account):
    fname = input("First name:")
    lname = input("Last name:")
    pnum = input("Phone number:")
    address = input("Address:")
    account_type = 1 # 0 for customer, 1 for official, 2 for admin
    official_id = logged_in_account['account_num']
    official_fname = logged_in_account['fname']
    official_lname = logged_in_account['lname']
    balance = 0
    username = input("Username: ")
    password = input ("Password: ")
    open_account(fname, lname, pnum, address, account_type, official_id, official_fname, official_lname, balance, username, password)
    print("Account created")

# return the username of a customer account given the first name, last name, and date of borth
def get_username():
    fname = input("First name:")
    lname = input("Last name:")
    dob = input("Date of birth: (YYYY-MM-DD)")
    for i in data:
        if data[i]['fname'] == fname and data[i]['lname'] == lname and data[i]['dob'] == dob:
            print(data[i]['username'])
            return
    print("Account not found")

# changes the status of an official account to closed if open and vice versa.
def change_status_official(account_num):
    if data[str(account_num)]['status'] == 0:
        data[str(account_num)]['status'] = 1
        print("Account opened")
    elif data[str(account_num)]['status'] == 1:
        data[str(account_num)]['status'] = 0
        print("Account closed")
    save_file(data)

