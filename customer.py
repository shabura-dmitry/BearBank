from fileloading import *
#Project Name: Bear Bank
#Team: Dmitry Shabura - ds227s@missouristate.edu
#      Myca Defoore - mgd4s@missouristate.edu
#      Katherine Austin - katherine117@live.missouristate.edu
# Fall 2023
data = load_file()

def change_pass(logged_in_account):
    new_pass = input("Please enter a new password:")
    logged_in_account['password'] = new_pass
    print("Password changed\n")
    save_file(data)
   
def check_transactions(): #create some transactions first
    print("unimplemented\n")

def view_account(logged_in_account):
    #print account data formatted nicely
    print("Account number:", logged_in_account['account_num'], "\nFirst name:", logged_in_account['fname'], "\nLast name:", 
    logged_in_account['lname'], "\nPhone number:", logged_in_account['pnum'], "\nAddress:", logged_in_account['address'], "\nAccount type:", 
    logged_in_account['account_type'], "\nOfficial id:", logged_in_account['official_id'], "\nOfficial first name:", 
    logged_in_account['official_fname'], "\nOfficial last name:", logged_in_account['official_lname'], "\nBalance:", 
    logged_in_account['balance'], "\nUsername:", logged_in_account['username'], "\nPassword:", logged_in_account['password'], "\nOpen date:", 
    logged_in_account['open_date'], "\nClose date:", logged_in_account['close_date'], "\nStatus:", logged_in_account['status'], "\nLast login:", 
    logged_in_account['last_login'], "\nDate of birth:", logged_in_account['dob'], "\n")