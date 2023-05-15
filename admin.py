import json
from account import open_account
from fileloading import *
from datetime import date
#Project Name: Bear Bank
#Team: Dmitry Shabura - ds227s@missouristate.edu
#      Myca Defoore - mgd4s@missouristate.edu
#      Katherine Austin - katherine117@live.missouristate.edu
# Fall 2023
data=load_file()

def open_official(logged_in_account):
    fname = input("First name:")
    lname = input("Last name:")
    pnum = input("Phone number:")
    address = input("Address:")
    account_type = 1 # 0 for customer, 1 for official, 2 for admin
    official_id = logged_in_account['account_num']
    official_fname = logged_in_account['fname']
    official_lname = logged_in_account['lname']
    balance = 0
    username = input("Username: ")
    password = input ("Password: ")
    open_account(fname, lname, pnum, address, account_type, official_id, official_fname, official_lname, balance, username, password)
    print("Account created\n")

# return the username of a customer account given the first name, last name
def get_username():
    fname = input("First name:")
    lname = input("Last name:")
    for i in data:
        if data[i]['fname'] == fname and data[i]['lname'] == lname:
            print("Username:", data[i]['username'])
            return
    print("Account not found\n")

# changes the status of an official account to closed if open and vice versa.
def change_status_official():
    account_num = input("Official account number:")
    #check if account type is official
    if data[str(account_num)]['account_type'] == 1:
        if data[str(account_num)]['status'] == 0:
            data[str(account_num)]['status'] = 1
            print("Account opened")
        elif data[str(account_num)]['status'] == 1:
            data[str(account_num)]['status'] = 0
            data[str(account_num)]['close_date'] = str(date.today())
            print("Account closed")
        save_file(data)

def change_pass_as_admin():
    account_num = input("Account number:")
    new_pass = input("Please enter a new password:")
    data[str(account_num)]['password'] = new_pass
    print("Password changed\n")
    save_file(data)
