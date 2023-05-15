from login import log_in, get_valid
from menu import create_menu

logged_in_account = log_in()

while get_valid() == False:
    logged_in_account = log_in()

create_menu(logged_in_account)
    