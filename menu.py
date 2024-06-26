from fileloading import load_file
from official import change_status_customer, open_customer, deposit_money, search_accounts
from admin import *
from customer import *
from datetime import date
#Project Name: Bear Bank
#Team: Dmitry Shabura - ds227s@missouristate.edu
#      Myca Defoore - mgd4s@missouristate.edu
#      Katherine Austin - katherine117@live.missouristate.edu
# Fall 2023
data = load_file()

#this function creates a menu based on the account type
def create_menu(logged_in_account):
     # if account type is 0, then it is a customer. if account type is 1, then it is an official. if account type is 2, then it is an admin
    account_type = logged_in_account['account_type']
    print("---Welcome to BearBank!---\n")
    # customer menu options: change login password, view account, view transaction history
    if account_type == 0:
        command = input("Please choose an option below:\na: change login password\nb: view account\nc:view transaction history\n")
        if command == 'a':
            change_pass(logged_in_account)
        elif command == 'b':
            view_account(logged_in_account)
        elif command == 'c':
            check_transactions()
        else:
            print ("error")
        create_menu(logged_in_account)

    # official menu options: open customer account, change customer account status, search accounts, deposit
    elif account_type == 1:
        command = input("Please choose an option below:\na:Open customer account\nb:Change customer account status\nc:search accounts\nd:deposit\n")
        if command == 'a':
            open_customer(logged_in_account)
        elif command == 'b':
            change_status_customer()
        elif command == 'c':
            search_accounts()
        elif command == 'd':
            deposit_money()
        else:
            print ("error")
        create_menu(logged_in_account)

    # admin menu options: enable/disable official account, retrieve login id, change password
    elif account_type == 2:
        command = input("Please choose an option below:\na:Open official account\nb:Change official account status\nc:Retrieve login id\nd:Change password\n")
        if command == 'a':
            open_official(logged_in_account)
        elif command == 'b':
            change_status_official()
        elif command == 'c':
            get_username()
        elif command == 'd':
            change_pass_as_admin()
        else:
            print ("error")
        create_menu(logged_in_account)

    else:
        print("error")