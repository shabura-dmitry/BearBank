from account import open_account

def open_customer():
    fname = input("First name:")
    lname = input("Last name:")
    pnum = input("Phone number:")
    address = input("Address:")
    account_type = 0 # 0 for customer, 1 for official, 2 for admin - probably shouldn't 
    balance = float(input("Enter initial deposit: "))
    open_account(fname, lname, pnum, address, account_type, balance)

def close_account(): #don't delete, just change status
    pass

def deposit_money(): #verify user login for this
    pass #update balance

def search_accounts():
    pass
open_customer()