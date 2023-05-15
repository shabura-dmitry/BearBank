from login import log_in
from menu import create_menu
from fileloading import encrypt_database

logged_in_account = log_in()
create_menu(logged_in_account)
