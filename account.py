import json


def open_account(fname, lname, pnum, address, account_type):
    filename = "C:/Users/ds227s/Documents/GitHub/BearBank/user_database.json"

    open_date = 0 #get current date
    close_date = -1 #dont change until closed
    balance = 0 
    #transaction_records = [] # unsure how to implement
    account_num = 0 # increment for every account made
    status = 1 # for closed, 1 for open
    account = {'fname': fname, 'lname': lname, 'pnum': pnum, 'address': address, 'open_date': open_date, 
               'close_date': close_date, 'balance': balance,
               'account_num': account_num, 'status': status, 'account_type': account_type}

    with open(filename, 'a', encoding="utf8") as outfile:
        json.dump(account, outfile)
    return account
    
    
    
open_account()



