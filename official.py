import json
from account import open_account

def fdf():
    fname = input("First name:")
    lname = input("Last name:")
    pnum = input("Phone number:")
    address = input("Address:")
    open_date = 0 #get current date
    close_date = -1 #dont change until closed
    balance = 0 
    transaction_records = [] # unsure how to implement
    account_num = 0 # increment for every account made
    status = 1 # for closed, 1 for open
    account_type = 0 # 0 for customer, 1 for official, 2 for admin - probably shouldn't 
    open_account(fname, lname, pnum)

def close_account(): #don't delete, just change status
    pass

def deposit_money(): #verify user login for this
    pass #update balance

def search_accounts():
    pass
