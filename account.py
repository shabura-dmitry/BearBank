from datetime import date
from fileloading import *
def open_account(fname, lname, pnum, address, account_type, balance, username, password):
    open_date = str(date.today())
    close_date = -1 #dont change until closed
    account_num = len(load_file())+1
    status = 1 # 0 for closed, 1 for open
    account = {
        "fname": fname,
        "lname": lname,
        "pnum": pnum,
        "address": address,
        "open_date": open_date,
        "close_date": close_date,
        "balance": balance,
        "account_num": account_num,
        "status": status,
        "account_type": account_type,
        "username": username,
        "password": password
        }
    add_account(account_num, account)
