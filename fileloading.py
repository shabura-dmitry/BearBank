import json
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'user_database.json')

def load_file():
    with open(filename, 'r', encoding="utf8") as data:
        data = json.load(data)
    return data

def save_file(data):
    with open(filename, 'w', encoding="utf8") as f:
        json.dump(data, f, indent=4)
        
#def create_database(data_structure):
#    with open(filename, 'w', encoding="utf8") as f:
#        json.dump(data_structure, f, indent=4)
        

#this is the dictionary for an account
account = {
        "fname": "fname",
        "lname": "lname",
        "pnum": "pnum",
        "address": "address",
        "open_date": "open_date",
        "close_date": "close_date",
        "balance": "balance",
        "account_num": "account_num",
        "status": "status",
        "account_type": "account_type",
        "username": "username",
        "password": "password"
        }

#this is the dictionary that holds all the accounts
data = load_file()

#add an account to the database
def add_account(account_num, account):
    data[account_num] = account
    save_file(data)

#create_database(data_structure)
#add_account(1,account)
#add_account(2,account)