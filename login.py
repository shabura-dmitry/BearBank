from fileloading import load_file
data = load_file()
print("Please enter a username and password")
username = input("Username:")
password = input("Password:")
filename = "C:/Users/ds227s/Documents/GitHub/BearBank/user_database.json"
def login(username, password):
    for account in range(len(data)):
        if data['username'] == username and data['password'] == password:
            #return the actual account array ex: account = data['account'][account_num]
            create_menu(data['account_type'])
    else:
        print("invalid username or password")

login(username, password)

def create_menu(account_type):
    if account_type == 0:
        print("Please choose an option below:")
        print("""
              a: change login password
              b: """")
    elif account_type == 1:
        print("Please choose an option below:")
        print("""
              a:open/close account
              b:search closed account
              c:search account
              d:deposit""")
    elif account_type ==2:
        print("Please choose an option below:")
        print ("""
               a:enable/disable official account
               b:retrieve login id
               c:change password""")
    else:
        print("error")