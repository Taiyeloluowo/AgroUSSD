from user import Farmer
from user import Customer
from USSDinterface import main_menu

ussd_code = '*123#'

print('================== AGRO USSD ==================')
print('Welcome to Agro USSD a platform that connects Farmers with consumers directly. Dial *123# to get started\n')

main_menu(ussd_code)
