from account import open_account
from fileloading import *
from datetime import date

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

# closes an account by changing the status to 0
def close_account(account_num): 
    data[account_num]['status'] = 0
    data[account_num]['close_date'] = str(date.today())
    save_file(data)

    

def deposit_money(account_num, amount):
    data[account_num]['balance'] += amount
    save_file(data)
    

def search_accounts():
    pass