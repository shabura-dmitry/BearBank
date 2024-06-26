from datetime import date
from fileloading import *
#Project Name: Bear Bank
#Team: Dmitry Shabura - ds227s@missouristate.edu
#      Myca Defoore - mgd4s@missouristate.edu
#      Katherine Austin - katherine117@live.missouristate.edu
# Fall 2023
def open_account(fname, lname, pnum, address, account_type, official_id, official_fname, official_lname, balance, username, password):
    open_date = str(date.today())
    close_date = -1 #dont change until closed
    account_num = len(load_file())+1
    status = 1 # 0 for closed, 1 for open
    last_login = -1 #dont change until logged in
    account = {
        "fname": fname,
        "lname": lname,
        "pnum": pnum,
        "address": address,
        "dob": open_date, #change later to input
        "open_date": open_date,
        "close_date": close_date,
        "last_login": last_login, #change later to input
        "balance": balance,
        "account_num": account_num,
        "official_id": official_id,
        "official_fname": official_fname,
        "official_lname": official_lname,
        "status": status,
        "account_type": account_type,
        "username": username,
        "password": password
        }
    add_account(account_num, account)