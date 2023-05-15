from login import log_in, get_valid
from menu import create_menu
#Project Name: Bear Bank
#Team: Dmitry Shabura - ds227s@missouristate.edu
#      Myca Defoore - mgd4s@missouristate.edu
#      Katherine Austin - katherine117@live.missouristate.edu
# Fall 2023
logged_in_account = log_in()

while get_valid() == False:
    logged_in_account = log_in()

create_menu(logged_in_account)
    