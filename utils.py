import csv

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