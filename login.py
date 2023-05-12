from fileloading import load_file
data = load_file()
print("Please enter a username and password")
username = input("Username:")
password = input("Password:")
filename = "C:/Users/ds227s/Documents/GitHub/BearBank/user_database.json"
def login(username, password):
    for account in range(len(data)):
        if data['username'] == username and data['password'] == password:
            create_menu(data['account_type'])
    else:
        print("invalid username or password")

login(username, password)

def create_menu(account_type):
    command = 0
    if account_type == 0:
        print("Please choose an option below:")
        print("""
              a: change login password
              b: view account
              c:view transaction history""")
        if command == 'a':
            pass
        elif command == 'b':
            pass
        elif command == 'c':
            pass
        else:
            print ("error")
    elif account_type == 1:
        print("Please choose an option below:")
        print("""
              a:open//close account
              b:search closed account
              c:search account
              d:deposit""")
        if command == 'a':
            pass
        elif command == 'b':
            pass
        elif command == 'c':
            pass
        elif command == 'd':
            pass
        else:
            print ("error")
    elif account_type ==2:
        print("Please choose an option below:")
        print ("""
               a:enable/disable official account
               b:retrieve login id
               c:change password""")
        if command == 'a':
            pass
        elif command == 'b':
            pass
        elif command == 'c':
            pass
        else:
            print ("error")
    else:
        print("error")