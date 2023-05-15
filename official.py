from account import open_account
from fileloading import *
from datetime import date
from login import log_in

data=load_file()
#open a customer account
def open_customer(logged_in_account):
    fname = input("First name:")
    lname = input("Last name:")
    pnum = input("Phone number:")
    address = input("Address:")
    account_type = 0 # 0 for customer, 1 for official, 2 for admin
    official_id = logged_in_account['account_num']
    official_fname = logged_in_account['fname']
    official_lname = logged_in_account['lname']
    balance = 0
    username = input("Username: ")
    password = input ("Password: ")
    open_account(fname, lname, pnum, address, account_type, official_id, official_fname, official_lname, balance, username, password)
    print("Account created")

# changes the status of a customer account to closed if open and vice versa.
def change_status_customer(account_num):
    if data[str(account_num)]['status'] == 0:
        data[str(account_num)]['status'] = 1
        print("Account opened")
    elif data[str(account_num)]['status'] == 1:
        data[str(account_num)]['status'] = 0
        print("Account closed")
    save_file(data)


def deposit_money(account_num, amount): 
    account = log_in()
    if account['status'] == 1:
        data[str(account_num)]['balance'] += amount
        print("Deposit successful")
    
# search by fname, lname, account number. return only account number, account holder information, opening and close dates, name and id of the bank official involved
def search_accounts():
    search = input("Search by:\na: first name\nb: last name\nc: account number\n")
    if search == 'a':
        fname = input("First name:")
        for i in data:
            if data[i]['fname'] == fname:
                print("First name:", data[i]['fname'], "\nLast name:", data[i]['lname'], "\nAccount number:", data[i]['account_num'], "\nOpen date:", 
                data[i]['open_date'], "\nClose date:", data[i]['close_date'], "\nOfficial id:", data[i]['official_id'], "\nOfficial first name:", 
                data[i]['official_fname'], "\nOfficial last name:", data[i]['official_lname'])

    elif search == 'b':
        lname = input("Last name:")
        for i in data:
            if data[i]['lname'] == lname:
                print("First name:", data[i]['fname'], "\nLast name:", data[i]['lname'], "\nAccount number:", data[i]['account_num'], "\nOpen date:", 
                data[i]['open_date'], "\nClose date:", data[i]['close_date'], "\nOfficial id:", data[i]['official_id'], "\nOfficial first name:", 
                data[i]['official_fname'], "\nOfficial last name:", data[i]['official_lname'])
    elif search == 'c':
        account_num = input("Account number:")
        for i in data:
            if data[i]['account_num'] == account_num:
                print("First name:", data[i]['fname'], "\nLast name:", data[i]['lname'], "\nAccount number:", data[i]['account_num'], "\nOpen date:", 
                data[i]['open_date'], "\nClose date:", data[i]['close_date'], "\nOfficial id:", data[i]['official_id'], "\nOfficial first name:", 
                data[i]['official_fname'], "\nOfficial last name:", data[i]['official_lname'])
    else:
        print("Invalid input")
        search_accounts()