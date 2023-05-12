import json
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'user_database.json')

def load_file():
    with open(filename, 'r', encoding="utf8") as data:
         data = json.load(data)
    return data

def save_file(data):
    with open(filename, 'w', encoding="utf8"):
        json.dumps(data)
        
def create_database(data_structure):
    with open(filename, 'w', encoding="utf8"):
        json.dumps(data_structure)
        
data_structure = {
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
create_database(data_structure)