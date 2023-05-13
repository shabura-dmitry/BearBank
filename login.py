from fileloading import load_file
from official import *
from admin import *
from customer import *
data = load_file()
print("Please enter a username and password")
#username = input("Username:")
#password = input("Password:")
username = 'u'
password = 'p'
def login(username, password):
    valid = False
    for i in data:
        if data[i]['username'] == username and data[i]['password'] == password:
            valid = True
            print("Login successful")
            return data[i]
        
    if valid == False:
        print("Invalid username or password")
    
   


#this function creates a menu based on the account type
def create_menu(account):
    print("create menu")
    account_type = account['account_type']
    account_num = account['account_num']
    # if account type is 0, then it is a customer. if account type is 1, then it is an official. if account type is 2, then it is an admin
    # customer menu options: change login password, view account, view transaction history
    if account_type == 0:
        command = input("Please choose an option below:\na: change login password\nb: view account\nc:view transaction history")
        if command == 'a':
            change_pass(username, password)
        elif command == 'b':
            view_account(account_num)
        elif command == 'c':
            pass
        else:
            print ("error")
    # official menu options: open/close account, search closed account, search account, deposit        
    elif account_type == 1:
        command = input("Please choose an option below:\na:Open customer account\nb:Close customer account\nc:search account\nd:deposit")
        if command == 'a':
            open_customer()
        elif command == 'b':
            close_customer(account_num)
        elif command == 'c':
            pass
        elif command == 'd':
            deposit_money()
        else:
            print ("error")
    # admin menu options: enable/disable official account, retrieve login id, change password
    elif account_type ==2:
        command = input("Please choose an option below:\na:enable official account\nb:disable official account\nc:retrieve login id\nd:change password")
        if command == 'a':
            enable_official()
        elif command == 'b':
            disable_official()
        elif command == 'c':
            retrieve_login()
        elif command == 'd':
            change_pass()
        else:
            print ("error")
    else:
        print("error")

create_menu(login(username, password))