from account import open_account
from fileloading import *
from datetime import date
from login import login
data=load_file()
def open_customer():
    fname = input("First name:")
    lname = input("Last name:")
    pnum = input("Phone number:")
    address = input("Address:")
    account_type = 0 # 0 for customer, 1 for official, 2 for admin - probably shouldn't 
    balance = float(input("Enter initial deposit: "))
    username = input("Username: ")
    password = input ("Password: ")
    open_account(fname, lname, pnum, address, account_type, balance, username, password)

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
    account = login()
    if account['status'] == 1:
        data[str(account_num)]['balance'] += amount
        print("Deposit successful")
    
def search_accounts():
    pass