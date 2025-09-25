import csv

from USSDinterface import farmer_menu
from user import Farmer

def checkIfHeaderExists(file, header):
    with open(file, "r", newline="") as f:
        reader = csv.reader(f)
        first_row = next(reader, None)
        if first_row == header:
            return True
        else:
            return False
        

def checkIfPhoneNumberExists(file, phoneNummber):
    with open(file, "r") as f:
        content = f.read()
        if phoneNummber in content:
            return True
        else:
            return False

def Login(farmer_filepath):
    user_phone = input('Enter your phone Number: ')
    user_pin = input('Enter your pin: ')

    user_dict = get_user_by_phone(farmer_filepath, user_phone)

    if user_dict:
        if user_pin == user_dict['pin']:
            current_user = Farmer(user_dict['name'], user_dict['phone'], user_dict['location'], user_dict['pin'], user_dict['size'], user_dict['crops'])
            print('======================================')
            print(f'Welcome, {user_dict['name']}')
            print('======================================')
            farmer_menu()
        else:
            print('Invalid phone number or pin')
# def findLineNumberOfUser(phoneNummber, file):

#     with open(file, "r", newline="") as f:
#         reader = csv.reader(f)
#         for row_num, row in enumerate(reader, start=1):
#             if text_to_find in row:
#                 return [row_num, row]
#             else:
#                 return  'User Not Found!'


def get_user_by_phone(filename, phone_number):
    with open(filename, "r", newline="") as f:
        reader = csv.DictReader(f) 
        for row in reader:
            if row["phone"] == phone_number: 
                return row
    return None

# Example usage
# user = get_user_by_phone("myfile.csv", "08012345678")

# if user:
#     print("User found:", user)
# else:
#     print("User not found.")
