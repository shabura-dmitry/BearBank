from login import log_in, valid
from menu import create_menu

logged_in_account = log_in()
if valid == True:
	create_menu(logged_in_account)
