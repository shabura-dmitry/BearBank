import json
import os

#get the path of the file
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'user_database.json')

def load_file():
    with open(filename, 'r', encoding="utf8") as data:
        data = json.load(data)
    return data

def save_file(data):
    with open(filename, 'w', encoding="utf8") as f:
        json.dump(data, f, indent=4)
        
# create a new database        
#def create_database(data_structure):
#    with open(filename, 'w', encoding="utf8") as f:
#        json.dump(data_structure, f, indent=4)


#add an account to the database
def add_account(account_num, account):
    data = load_file()
    data[account_num] = account
    save_file(data)
