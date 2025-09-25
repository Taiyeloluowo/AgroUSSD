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

def getUserInfo(file, phoneNumber, password, userType):
    with open(file, "r+") as f:
        content = f.readlines()
        # print(content)
        currentUser = {}
        userInfo = []
        try:
            for item in content:
                phone = phoneNumber in item
                if phone:
                    userInfo = content[content.index(item)].split(',')
                    break
                else:
                    continue
        except Exception as e:
            print('Phone Number not found')
        
        if userInfo:
            if userType == 'farmer':
                currentUser["name"] = userInfo[0]
                currentUser["phone"] = userInfo[1]
                currentUser["location"] = userInfo[2]
                currentUser["pin"] = userInfo[3]
                currentUser["size"] = userInfo[4]
                currentUser["crops"] = userInfo[5]
            else:
                currentUser["name"] = userInfo[0]
                currentUser["phone"] = userInfo[1]
                currentUser["location"] = userInfo[2]
                currentUser["pin"] = userInfo[3]
                
            if password == currentUser["pin"].splitlines()[0]:
                return currentUser
            else:
                return "Invalid Password or Phone Number"
        # print(content)