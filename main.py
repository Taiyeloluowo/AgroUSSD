from classes import Farmer


entry = input("Would you like to register or log in? ")
if entry == "register":
    Farmer.register()
elif entry == "log in":
    print("Thank you for using this service")
    