from pathlib import Path
from utils import Login, checkIfHeaderExists
from utils import checkIfPhoneNumberExists
# from utils import findLineNumberOfUser
from USSDinterface import farmer_menu
from utils import get_user_by_phone
import csv


Database = Path ("database")
Database.mkdir(exist_ok = True)
farmer_filepath = Database / "farmer.csv"
customer_filepath = Database / "customer.csv"

class User:
    def __init__(self, name, phone_number, location, pin):
        self.name = name
        self.phone_number = phone_number
        self.location = location
        self.pin = pin
        

class Farmer(User):
    def __init__(self, name, phone_number, location, pin, farm_size, primary_crops):
        super().__init__(name, phone_number, location, pin)
        self.farm_size = farm_size
        self.primary_crops = primary_crops

    def register():
        name = input("Enter your name: ")
        while True:
            phone = input("Enter your phone number: ")
            if checkIfPhoneNumberExists(farmer_filepath, phone):
                print('❌❌ Phone Number already exist')
                continue
            else:
                location = input("What is your location: ")
                pin = input("Enter your pin: ")
                size = input("Enter your famr size: ")
                crops = input("What is your primary crop? ")
                break
        data = [name, phone, location, pin, size, crops]
        with open(farmer_filepath, 'a', encoding= "utf=8", newline="") as f:
            header = ["name", "phone", "location", "pin", "size", "crops"]
            headerExist = checkIfHeaderExists(farmer_filepath, header)
            writer = csv.writer(f)
            if not headerExist:
                writer.writerow(header)
            writer.writerow(data)
        print("Registered Successfully ✅✅")

    def login():
        Login(farmer_filepath)

class Customer(User):
    def __init__(self, name, phone_number, location, pin):
        super().__init__(name, phone_number, location, pin)

    def register():
        name = input("Enter your name: ")
        while True:
            phone = input("Enter your phone number: ")
            if checkIfPhoneNumberExists(customer_filepath, phone):
                print('❌❌ Phone Number already exist')
                continue
            else:
                location = input("What is your location: ")
                pin = input("Enter your pin: ")
                break
        
        header = ['name', 'phone', 'location', 'pin']
        data = [name, phone, location, pin]
        with open(customer_filepath, 'a', encoding= "utf=8", newline="") as f:
            headerExist = checkIfHeaderExists(customer_filepath, header)
            writer = csv.writer(f)
            if not headerExist:
                writer.writerow(header)
            writer.writerow(data)
        print("Registered Successfully ✅✅")