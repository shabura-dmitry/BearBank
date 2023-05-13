import json
from account import open_account
def create_official():
    fname = input("First name:")
    lname = input("Last name:")
    pnum = input("Phone number:")
    address = input("Address:")
    #transaction_records = [] # unsure how to implement
    status = 1 # 0 for closed, 1 for open
    account_type = 1 # 0 for customer, 1 for official, 2 for admin - probably shouldn't 
    open_account(fname, lname, pnum, address, account_type, status)

def get_username(fname, lname):
    pass

def change_password():
    pass

def enable_official():
    pass

def disable_official():
    pass

def retrieve_login():
    pass

