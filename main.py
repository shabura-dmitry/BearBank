from login import log_in, get_valid
from menu import create_menu

logged_in_account = log_in()
if get_valid() == True:
	create_menu(logged_in_account)
