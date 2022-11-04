#Bryan Lor - Week 9 Lab Assignment
import random
import decimal

def generateID(dictionary):
    uniqueID = decimal.Decimal(random.uniform(100, 500))
    # If the generated ID is already in the dictionary, it will continue to generate new IDs until its found a unique one
    while uniqueID in dictionary:
        uniqueID = decimal.Decimal(random.uniform(100, 500))
    return uniqueID

def inputString(name, allowNumbers = True):
    string = input("Enter The " + name + ": ")
    # This will check to see if there are any digits inside the input and will reprompt it to the user
    while (any(char.isdigit() for char in string)) and not allowNumbers:
        string = input("ERROR: " + name + " Cannot Contain Numerical Values, Try Again\n\nEnter The " + name + ": ")
    return string

def inputAddress():
    address = input("Enter The Address: ")
    return address

def inputNumbers(name, length):
    numbers = input("Enter The " + name + ": ")
    while numbers.isdigit() == False:
        numbers = input("ERROR: " + name + " Must Be Only Digits, Try Again\n\nEnter The " + name + ": ")
    while len(numbers) != length:
        numbers = input("ERROR: " + name + " Must Meet " + 
        str(length) + " Digits, Try Again\n\nEnter The " + name + ": ")
    return numbers

def inputStatus(name):
    string = input("Enter The " + name + ": ").lower()
    # This will check to see if there are any digits inside the input and will reprompt it to the user
    while (any(char.isdigit() for char in string)):
        string = input("ERROR: " + name + " Cannot Contain Numerical Values, Try Again\n\nEnter The " + name + ": ").lower()
    # This will reprompt the user until it has a y or n inside the string
    while "y" not in string and "n" not in string:        
        string = input("ERROR: " + name + " Must Contain Y or N, Try Again\n\nEnter The " + name + ": ")
    if "y" in string:
        return "Yes"
    else:
        return "No"

def addUsers(employees, amount):
    user = {}
    i = 1
    while i <= amount:
        uniqueID = generateID(employees)
        user["Name"] = inputString("Name", False)
        user["Address"] = inputAddress()
        user["Phone"] = inputNumbers("Phone Number", 10)
        user["SSN"] = inputNumbers("SSN", 9)
        user["Manager Status"] = inputStatus("Manager Status")
        user["Job Title"] = inputString("Job Title")
        user["Skills"] = inputString("Skills")

        print(user, "\n")
        employees[uniqueID] = user
        i += 1

def query(employees, name):
    x = input("    Enter The " + name +": ").lower()
    for user in employees:
        if x in employees[user][name].lower():
            print("    ", employees[user])

def main():
    employees = {}
    addUsers(employees, 3)

    # # Set Of Premade Examples To Quickly Run Queries 
    # employees = {
    #     decimal.Decimal('312.64094046597716669566580094397068023681640625') : {'Name': 'Bryan', 'Address': '123 AWD', 'Phone': '5863921203', 'SSN': '122938004', 'Manager Status': 'No', 'Job Title': 'Student', 'Skills': 'Programming'},
    #     decimal.Decimal('152.1534073114722787067876197397708892822265625') : {'Name': 'Cameron', 'Address': '938 AWD', 'Phone': '5862938122', 'SSN': '993085442', 'Manager Status': 'Yes', 'Job Title': 'Chef', 'Skills': 'Cooking'},
    #     decimal.Decimal('429.37705388297814579345867969095706939697265625') : {'Name': 'Emily', 'Address': '389 AWD', 'Phone': '3132938842', 'SSN': '880344291', 'Manager Status': 'Yes', 'Job Title': 'Graphic Designer', 'Skills': 'Art'}
    # }

    while True:
        for user in employees:
            print(user)
            print(employees[user])

        print("\n\nWhat Do You Want To Do?\n-------------------------\n1. Query by Name\n2. Query by Skills\n3. Query by Manager Status\n0. Quit")
        x = input("Enter [0-3]: ")
        match x:
            case "0":
                break
            case "1":
                query(employees, "Name")
            case "2":
                query(employees, "Skills")
            case "3":
                query(employees, "Manager Status")
            case other:
                print("ERROR: Must Enter 0-3, Try Again.")
        print()

main()