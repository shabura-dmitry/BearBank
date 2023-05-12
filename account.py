from datetime import date
from fileloading import load_file
from fileloading import save_file
def open_account(fname, lname, pnum, address, account_type, balance, username, password):
    data = load_file()
    open_date = str(date.today())
    close_date = -1 #dont change until closed
    account_num = len(data)+1
    status = 1 # 0 for closed, 1 for open
    account = {'fname': fname, 'lname': lname, 'pnum': pnum, 'address': address, 'open_date': open_date, 
               'close_date': close_date, 'balance': balance,'account_num': account_num,
                'status': status, 'account_type': account_type, 'username': username, 'password': password}
    data[account_num] = account
    
    save_file(data)
