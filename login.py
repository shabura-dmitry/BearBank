from fileloading import load_file
from official import *
from admin import *
from customer import *
data = load_file()

def login():
    print("Please enter a username and password")
    #username = input("Username:")
    #password = input("Password:")
    username = 'u'
    password = 'p'
    valid = False
    for i in data:
        if data[i]['username'] == username and data[i]['password'] == password:
            valid = True
            print("Login successful")
            data[i]['last_login'] = str(date.today())
            print("Last login: " + data[i]['last_login'] + "\n")
            return data[i]
        
    if valid == False:
        print("Invalid username or password")
    

#this function creates a menu based on the account type
def create_menu(account):
     # if account type is 0, then it is a customer. if account type is 1, then it is an official. if account type is 2, then it is an admin
    account_type = account['account_type']
    account_num = account['account_num']
   
    # customer menu options: change login password, view account, view transaction history
    if account_type == 0:
        command = input("Please choose an option below:\na: change login password\nb: view account\nc:view transaction history")
        if command == 'a':
            change_pass()
        elif command == 'b':
            view_account(account_num)
        elif command == 'c':
            check_transactions(account_num)
        else:
            print ("error")

    # official menu options: open customer account, enable/disable customer account, search account, deposit        
    elif account_type == 1:
        command = input("Please choose an option below:\na:Create customer account\nb:open or close customer account\nc:search account\nd:deposit")
        if command == 'a':
            open_customer()
        elif command == 'b':
            change_status_customer(account_num)
        elif command == 'c':
            search_accounts()
        elif command == 'd':
            deposit_money(account_num)
        else:
            print ("error")
    # admin menu options: enable/disable official account, retrieve login id, change password
    elif account_type ==2:
        command = input("Please choose an option below:\na:Create official account\nb:Disable official account\nc:Retrieve login id\nd:Change password")
        if command == 'a':
            open_official()
        elif command == 'b':
            change_status_official(account_num)
        elif command == 'c':
            retrieve_login()
        elif command == 'd':
            change_pass(account_num)
        else:
            print ("error")
    else:
        print("error")

create_menu(login())