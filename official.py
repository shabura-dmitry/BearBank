from account import open_account
from fileloading import *
from datetime import date
from login import log_in
data=load_file()
def open_customer():
    fname = input("First name:")
    lname = input("Last name:")
    pnum = input("Phone number:")
    address = input("Address:")
    account_type = 0 # 0 for customer, 1 for official, 2 for admin
    balance = float(input("Enter initial deposit: "))
    username = input("Username: ")
    password = input ("Password: ")
    open_account(fname, lname, pnum, address, account_type, balance, username, password)
    print("Account created")

# changes the status of a customer account to closed if open and vice versa.
def change_status_customer(account_num):
    if data[str(account_num)]['status'] == 0:
        data[str(account_num)]['status'] = 1
        print("Account opened")
    elif data[str(account_num)]['status'] == 1:
        data[str(account_num)]['status'] = 0
        print("Account closed")
    save_file(data)


def deposit_money(account_num, amount): 
    account = log_in()
    if account['status'] == 1:
        data[str(account_num)]['balance'] += amount
        print("Deposit successful")
    

def search_accounts():
    search = input("Search by:\na: first name\nb: last name\nc: phone number\nd: address\ne: account number\n")
    if search == 'a':
        fname = input("First name:")
        for i in data:
            if data[i]['fname'] == fname:
                print(data[i])
    elif search == 'b':
        lname = input("Last name:")
        for i in data:
            if data[i]['lname'] == lname:
                print(data[i])
    elif search == 'c':
        pnum = input("Phone number:")
        for i in data:
            if data[i]['pnum'] == pnum:
                print(data[i])
    elif search == 'd':
        address = input("Address:")
        for i in data:
            if data[i]['address'] == address:
                print(data[i])
    elif search == 'e':
        account_num = input("Account number:")
        for i in data:
            if data[i]['account_num'] == account_num:
                print(data[i])
    else:
        print("Invalid input")
        search_accounts()