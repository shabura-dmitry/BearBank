import json
from datetime import date

def open_account(fname, lname, pnum, address, account_type, balance):
    

    open_date = str(date.today())
    close_date = -1 #dont change until closed
    balance = 0 
    account_num = 0 # increment for every account made
    status = 1 # 0 for closed, 1 for open
    account = {'fname': fname, 'lname': lname, 'pnum': pnum, 'address': address, 'open_date': open_date, 
               'close_date': close_date, 'balance': balance,
               'account_num': account_num, 'status': status, 'account_type': account_type}
    
   
    return account
