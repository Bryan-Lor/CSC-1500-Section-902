# Bryan Lor - Database Functions  --------------------------------------
import pandas
import os
import random
import tkinter as tk
from tkinter import filedialog
from tabulate import *
import copy

IS_REVERSED = False
ID_LENGTH = 9

DEFAULT_FIELDS = {
    'userID': {},
    'name': {},
    'position': {},
    'SSN': {},
    'home address': {},
    'email': {},
    'phone number': {},
    'skills': {}
 }
CUSTOMERS = copy.deepcopy(DEFAULT_FIELDS)
CUSTOMER = copy.deepcopy(DEFAULT_FIELDS)

# Dropdown menu options
QUERYTYPES = list(DEFAULT_FIELDS.keys())
OPTIONS = [
    "Display Database",
    "Add Customer",
    "Query Data",
    "Reverse Data",
]

# Prompts selecting a file through Windows Explorer
def askOpenFile():
    filePath = filedialog.askopenfilename(initialdir=os.getcwd())
    return filePath

# Reads excel sheet and calls extract data method
def readExcel(filePath):
    global CUSTOMERS
    excelData = pandas.read_excel(filePath)
    CUSTOMERS = excelData.to_dict()
    return tabulate(pandas.DataFrame(CUSTOMERS), headers='keys')

# Writes to text field widget
def writeToTextField(field, text, clear=True):
    field.config(state="normal")
    if clear: field.delete("0.0","end")
    field.insert(tk.INSERT, text + "\n\n")
    field.config(state="disabled")

# Hides the data type widget
def toggleDataTypeWidget(widget, value = False):
    if not value: widget.grid_forget()
    else: widget.grid(row=0, column=1, sticky='w', padx=5, pady=5)

# Adds a new user to the database
def addUser(resultField, dataTypeText, inputField, filePath):
    global CUSTOMER
    global DEFAULT_FIELDS
    inputField = inputField.replace('-', '')

    # Checks to see if userID has anything inside and assign an entry ID accordingly
    if CUSTOMERS['userID'] == {}: entryID = 0
    else: entryID = len(CUSTOMERS['userID'])

    # Input Restrictions and displaying it
    # Attempted to manually create UniqueID
    if dataTypeText == QUERYTYPES[0]:
        writeToTextField(resultField, "Adding A New Customer. Enter Inputs For All Data Fields\n"+ tabulate(pandas.DataFrame(CUSTOMER), headers='keys'), True)    
        writeToTextField(resultField, "\nProgram will automatically generate ID, please fill in other fields.", False)
        writeToTextField(resultField, "Database:", False)      
        displayDatabase(resultField, CUSTOMERS, False)
        return
    # Entered empty input
    elif inputField == "":
        writeToTextField(resultField, "Adding A New Customer. Enter Inputs For All Data Fields\n"+ tabulate(pandas.DataFrame(CUSTOMER), headers='keys'), True)    
        writeToTextField(resultField, "\nYou Cannot Enter Empty Inputs", False)
        writeToTextField(resultField, "Database:", False)      
        displayDatabase(resultField, CUSTOMERS, False)
        return
    # Name and skills restriction
    elif dataTypeText == QUERYTYPES[1] and not isLettersOnly(inputField):
        writeToTextField(resultField, "Adding A New Customer. Enter Inputs For All Data Fields\n"+ tabulate(pandas.DataFrame(CUSTOMER), headers='keys'), True)    
        writeToTextField(resultField, "\n" + dataTypeText.capitalize() + " Cannot Contain Numerical Values and/or Special Characters", False)
        writeToTextField(resultField, "Database:", False)      
        displayDatabase(resultField, CUSTOMERS, False)
        return
    # SSN restriction
    elif dataTypeText == QUERYTYPES[3] and not isNumbers(inputField, 9):
        writeToTextField(resultField, "Adding A New Customer. Enter Inputs For All Data Fields\n"+ tabulate(pandas.DataFrame(CUSTOMER), headers='keys'), True)    
        writeToTextField(resultField, "\n" + dataTypeText.upper() + " Must Be Only Digits and 9 Numbers Long", False)
        writeToTextField(resultField, "Database:", False)      
        displayDatabase(resultField, CUSTOMERS, False)
        return
    # Email restriction
    elif dataTypeText == QUERYTYPES[5] and not isEmail(inputField):
        writeToTextField(resultField, "Adding A New Customer. Enter Inputs For All Data Fields\n"+ tabulate(pandas.DataFrame(CUSTOMER), headers='keys'), True)    
        writeToTextField(resultField, "\nInvalid " + dataTypeText.capitalize() + " Address", False)
        writeToTextField(resultField, "Database:", False)      
        displayDatabase(resultField, CUSTOMERS, False)
        return
    # Phone number restriction
    elif dataTypeText == QUERYTYPES[6] and not isNumbers(inputField, 10):
        writeToTextField(resultField, "Adding A New Customer. Enter Inputs For All Data Fields\n"+ tabulate(pandas.DataFrame(CUSTOMER), headers='keys'), True)    
        writeToTextField(resultField, "\n" + dataTypeText.capitalize() + " Must Be Only Digits and 10 Numbers Long", False)
        writeToTextField(resultField, "Database:", False)      
        displayDatabase(resultField, CUSTOMERS, False)
        return
    # Skills restriction
    elif dataTypeText == QUERYTYPES[7] and not isLettersOnly(inputField):
        writeToTextField(resultField, "Adding A New Customer. Enter Inputs For All Data Fields\n"+ tabulate(pandas.DataFrame(CUSTOMER), headers='keys'), True)    
        writeToTextField(resultField, "\n" + dataTypeText.capitalize() + " Cannot Contain Numerical Values and/or Special Characters", False)
        writeToTextField(resultField, "Database:", False)      
        displayDatabase(resultField, CUSTOMERS, False)
        return
    
    # Create unique ID if does not already have one
    if CUSTOMER['userID'] == {}:
        generatedID = generateID(ID_LENGTH)        
        # if ID in database, generate a new unique one
        while generatedID in CUSTOMERS['userID']: generatedID = generateID(ID_LENGTH)
        CUSTOMER['userID'] = {entryID: generatedID}
    CUSTOMER[dataTypeText] = {entryID : inputField} 

    # Display Database 
    writeToTextField(resultField, "Adding A New Customer. Enter Inputs For All Data Fields\n"+ tabulate(pandas.DataFrame(CUSTOMER), headers='keys'), True)    
    writeToTextField(resultField, "Database:", False)      
    displayDatabase(resultField, CUSTOMERS, False)

    # Assign Values and Save File if fully filled out
    if {} not in list(CUSTOMER.values()):
        # Else add all inputs into database
        for key,valueDict in CUSTOMER.items():
            CUSTOMERS[key][entryID] = valueDict[entryID]
        saveExcel(resultField, filePath, "\nEntry Successfully Saved and Added!")
        resetCustomer()
    return True
# Querys database by looking at its datatype and user input
def queryData(resultField, dataTypeText, inputField):
    queried_CUSTOMERS = copy.deepcopy(DEFAULT_FIELDS)
    values = list(CUSTOMERS[dataTypeText].values())
    values = [str(v).lower() for v in values]
    indexFound = []

    # Get index of customers with queried input
    for i in range(len(values)):
        if inputField.lower() in str(values[i].lower()):
            indexFound.append(i)

    # Assign values to query and display
    for index in indexFound:
        for key, valueDict in CUSTOMERS.items():
            queried_CUSTOMERS[key][index] = valueDict[index]
    writeToTextField(resultField, "Results: ", True)
    displayDatabase(resultField, queried_CUSTOMERS, False)
    writeToTextField(resultField, "Database:", False)
    displayDatabase(resultField, CUSTOMERS, False)

# Saves database to excel. Creates an excel sheet if filepath isn't specified
def saveExcel(resultField, filePath, text = "\nDatabase Successfully Saved!"):
    if filePath == "":   
        try:
            pandas.DataFrame(CUSTOMERS).to_excel(os.getcwd()+"\DefaultDataBase.xlsx", index=False)
        except:
            writeToTextField(resultField, "Issue Occured Saving/Adding Data. Please Make Sure Default DataFile Is Not Opened", True)
            return
    else:
        try:
            pandas.DataFrame(CUSTOMERS).to_excel(filePath, index=False)
        except:
            writeToTextField(resultField, "Issue Occured Saving/Adding Data. Please Make Sure Specified DataFile Is Not Opened", True)
            return        
    writeToTextField(resultField, text, True)        
    displayDatabase(resultField, CUSTOMERS,False)

# Displays database
def displayDatabase(resultField, database, value = True):
    writeToTextField(resultField, tabulate(pandas.DataFrame(database), headers='keys'), value)

# Reverse database
def reverseDatabase(resultField):
    global CUSTOMERS
    CUSTOMERS = dict(reversed(list(CUSTOMERS.items())))
    displayDatabase(resultField, CUSTOMERS)

# This will check to see if there are any digits inside the input and return a bool value
def isCharactersOnly(input):
    #while (any(char.isdigit() for char in input)): return False
    if (any(char.isdigit() for char in input)): return False
    return True

# This will make shure that only normal characters are inside and return bool values
def isLettersOnly(input):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ',',']
    if not isCharactersOnly(input):
        #print("Has Digit")
        return False

    for char in input:
        letter = char.lower()
        if letter not in letters:
            #print("Has special letters")
            return False
    return True

# This will check to make sure only digits were inputted and return a bool value
def isNumbers(input, length):
    if (any(not char.isdigit() for char in input)):
        return False
    if len(str(input)) != length:
        return False
    return True

# This will check to make email input has @ and . in it
def isEmail(input):
    if "@" in input and "." in input:
        return True
    else:
        return False

# Creates a random ID
def generateID(length):
    # Returns current ID if already has one
    if CUSTOMER['userID'] != {}: return CUSTOMER['userID']

    numbers = ['0','1','2','3','4','5','6','7','8','9']
    uniqueID = ""
    while len(uniqueID) < length: uniqueID += random.choice(numbers)
    return uniqueID

def resetCustomer():
    global CUSTOMER    
    CUSTOMER.clear()
    CUSTOMER = copy.deepcopy(DEFAULT_FIELDS)