import json
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'user_database.json')

def load_file():
    with open(filename, 'r', encoding="utf8") as data:
         data = json.load(data)
    return data

def save_file():
    with open(filename, 'w', encoding="utf8") as data:
        json.dump(data)