from user import Customer
from user import Farmer
from utils import Login

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
            elif user_option == '3':
                Farmer.login()
            elif user_option == '4':
                break
            else:
                print('==============================')
                print('Invalid input, pls try again!')
                print('==============================')

def farmer_menu():
    while True:
        print('\nSelect an option to continue')
        print('1. Add Harvest information')
        print('2. Set price for crop')
        print('3. Logout')
        user_option = input("Enter option: ")

        if user_option == '3':
            break
        else:
            print('==============================')
            print('Invalid input, pls try again!')
            print('==============================')