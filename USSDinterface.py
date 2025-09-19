from user import Customer
from user import Farmer

def main_menu(ussd_code):
    user_input = input('Enter code: ')
    while True:
        if user_input == ussd_code:
            print('Select an option to continue\n')
            print('1. Register as a farmer')
            print('2. Register as a customer')
            print('3. Login')
            print('4. Exit\n')
            user_option = input("Enter option: ")
            if user_option == '1':
                Farmer.register()
            elif user_option == '2':
                Customer.register()
            elif user_option == '4':
                break
            else:
                print('==============================')
                print('Invalid input, pls try again!')
                print('==============================')