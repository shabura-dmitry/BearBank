import json
fname = 0
lname = 0
pnum = 0
address = 0
open_date = 0
close_date = 0
balance = 0
transaction_records = 0
account_num = 0
status = 0
account_type = 0

account = {'fname': fname, 'lname': lname, 'pnum': pnum, 'address': address, 'open_date': open_date, 
           'close_date': close_date, 'balance': balance, 'transaction_records': transaction_records,
           'account_num': account_num, 'status': status, 'account_type': account_type}

filename = "C:/Users/ds227s/Documents/GitHub/BearBank/user_database.json"
with open(filename, 'a', encoding="utf8") as outfile:
    json.dump(account, outfile)
with open(filename) as infile:
    data = json.load(infile)
    
    