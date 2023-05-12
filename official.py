from account import open_account
from fileloading import load_file
data=load_file()
def open_customer():
    fname = input("First name:")
    lname = input("Last name:")
    pnum = input("Phone number:")
    address = input("Address:")
    account_type = 0 # 0 for customer, 1 for official, 2 for admin - probably shouldn't 
    balance = float(input("Enter initial deposit: "))
    open_account(fname, lname, pnum, address, account_type, balance)

def close_account(): #don't delete, just change status
    status = 0 #variable assigned but not used

def deposit_money(): #verify user login for this
    amount = float(input("Amount to deposit: "))
    data['balance'] = data['balance'] + amount
    

def search_accounts():
    pass
open_customer()