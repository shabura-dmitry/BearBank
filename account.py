fname = 0
lname = 0
pnum = 0
address = 0
open_date = 0
close_date = 0
balance = 0
transaction_records = []
account_num = 0
status = 0
account_type = 0

# going to try creating a dict for each account, converting to str for saving using json, then read file to recreate user database on program run
accounts = {1: {
                fname: "", lname: "", pnum: "", address: "", open_date: "", 
                close_date: "", balance: "", transaction_records: {},
                account_num: "", status: "", account_type: ""}}