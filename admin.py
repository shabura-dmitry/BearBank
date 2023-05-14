import json
from account import open_account
from fileloading import *

data=load_file()

def open_official():
    fname = input("First name:")
    lname = input("Last name:")
    pnum = input("Phone number:")
    address = input("Address:")
    #transaction_records = [] # unsure how to implement
    status = 1 # 0 for closed, 1 for open
    account_type = 1 # 0 for customer, 1 for official, 2 for admin - probably shouldn't 
    open_account(fname, lname, pnum, address, account_type, status)

def get_username(fname, lname, pnum):
    pass

# changes the status of an official account to closed if open and vice versa.
def change_status_official(account_num):
    if data[str(account_num)]['status'] == 0:
        data[str(account_num)]['status'] = 1
        print("Account opened")
    elif data[str(account_num)]['status'] == 1:
        data[str(account_num)]['status'] = 0
        print("Account closed")
    save_file(data)

# retrieves the login id of a customer account given the full name and date of birth
def retrieve_login():
    fname = input("First name:")
    lname = input("Last name:")
    dob = input("Date of birth:")
    for i in data:
        if data[i]['fname'] == fname and data[i]['lname'] == lname and data[i]['dob'] == dob:
            print(data[i]['username'])
            return
    print("Account not found")