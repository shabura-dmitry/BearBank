from fileloading import *
data = load_file()
#change the password of the account
def change_pass(username, password, account_num):
    #if username and password are correct for account_num then change the password
    if data[account_num]['username'] == username and data[account_num]['password'] == password:
        new_pass = input("Enter new password: ")
        data[account_num]['password'] = new_pass
        save_file(data)

def check_transactions(): #create some transactions first
    print("unimplemented")

def view_account(account_num):
    print(data[account_num])
    pass
