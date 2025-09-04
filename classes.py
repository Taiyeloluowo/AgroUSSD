from pathlib import Path
import csv


Database = Path ("database")
Database.mkdir(exist_ok = True)
filepath = Database / "users.csv"

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
        phone = input("Enter your phone number: ")
        location = input("What is your location: ")
        pin = input("Enter your pin: ")
        size = input("Enter your famr size: ")
        crops = input("What is your primary crop? ")
        data = [name, phone, location, pin, size, crops]
        with open(filepath, 'a', encoding= "utf=8") as f:
            writer = csv.writer(f)
            writer.writerows([data])