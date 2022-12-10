# Bryan Lor - Database Functions  --------------------------------------
import pandas
import os
import tkinter as tk
from tkinter import filedialog
from tabulate import *
import copy

DEFAULT_FIELDS = {
    'Title': {},
    'Author': {},
    'ISBN': {},
    'Purchased': {},
    'Checked Out': {},
    'Price': {},
 }
BOOKS = copy.deepcopy(DEFAULT_FIELDS)
BOOK = copy.deepcopy(DEFAULT_FIELDS)

# Dropdown menu options
QUERYTYPES = list(DEFAULT_FIELDS.keys())
OPTIONS = ["Query", "Add", "Edit", "Remove"]

# Prompts selecting a file through Windows Explorer
def askOpenFile():
    filePath = filedialog.askopenfilename(initialdir=os.getcwd())
    return filePath

# Reads excel sheet and calls extract data method
def readExcel(filePath):
    global BOOKS
    excelData = pandas.read_excel(filePath)
    BOOKS = excelData.to_dict()   

# Writes to text field widget
def writeToTextField(field, text, clear=True):
    field.config(state="normal")
    if clear: field.delete("0.0","end")
    field.insert(tk.INSERT, text + "\n\n")
    field.config(state="disabled")

# Hides the data type widget
def toggleQueryTypeWidget(widget, show = False):
    if show: widget.grid(row=0, column=1, sticky='e', padx=8, pady=5)
    else: widget.grid_forget() 

# Adds a new user to the database
def addEntry(resultField, dataTypeText, inputField, filePath):
    global BOOK
    global DEFAULT_FIELDS
    inputField = inputField.replace('-', '')

    # Assigns a unique identifier entryID based on amount of entries for ISBNs
    entryAmount = len(BOOKS["ISBN"].values())
    if entryAmount > 0:
        entryID = entryAmount
    else:
        entryID = 0

    if inputField == "":
        writeToTextField(resultField, "Adding A New Book. Enter Inputs For All Data Fields\n"+ tabulate(pandas.DataFrame(BOOK), headers='keys'), True)    
        writeToTextField(resultField, "\nYou Cannot Enter Empty Inputs", False)
        writeToTextField(resultField, "Database:", False)      
        displayDatabase(resultField, BOOKS, False)
        return False
    # Title and Author restriction - Letters Only
    elif dataTypeText == QUERYTYPES[1] and not isLettersOnly(inputField) or dataTypeText == QUERYTYPES[0] and not isLettersOnly(inputField):
        writeToTextField(resultField, "Adding A New Book. Enter Inputs For All Data Fields\n"+ tabulate(pandas.DataFrame(BOOK), headers='keys'), True)    
        writeToTextField(resultField, "\n" + dataTypeText.capitalize() + " Cannot Contain Numerical Values and/or Special Characters", False)
        writeToTextField(resultField, "Database:", False)      
        displayDatabase(resultField, BOOKS, False)
        return False
    # ISBN restriction - Numbers Only
    elif dataTypeText == QUERYTYPES[2] and not isNumbers(inputField):
        writeToTextField(resultField, "Adding A New Book. Enter Inputs For All Data Fields\n"+ tabulate(pandas.DataFrame(BOOK), headers='keys'), True)    
        writeToTextField(resultField, "\n" + dataTypeText.upper() + " Must Be Only Digits", False)
        writeToTextField(resultField, "Database:", False)      
        displayDatabase(resultField, BOOKS, False)
        return False
    # Purchased and Checked Out restriction - Integers only
    elif dataTypeText == QUERYTYPES[3] and not isInt(inputField) or dataTypeText == QUERYTYPES[4] and not isInt(inputField):
        writeToTextField(resultField, "Adding A New Book. Enter Inputs For All Data Fields\n"+ tabulate(pandas.DataFrame(BOOK), headers='keys'), True)    
        writeToTextField(resultField, "\n" + dataTypeText.capitalize() + " Must Be An Integer Value", False)
        writeToTextField(resultField, "Database:", False)      
        displayDatabase(resultField, BOOKS, False)
        return False
    # Price restriction - Float only
    elif dataTypeText == QUERYTYPES[5] and not isFloat(inputField):
        writeToTextField(resultField, "Adding A New Book. Enter Inputs For All Data Fields\n"+ tabulate(pandas.DataFrame(BOOK), headers='keys'), True)    
        writeToTextField(resultField, "\n" + dataTypeText.capitalize() + " Must Be A Float Value", False)
        writeToTextField(resultField, "Database:", False)      
        displayDatabase(resultField, BOOKS, False)
        return False

    BOOK[dataTypeText] = {entryID : inputField} 

    # Display Database 
    writeToTextField(resultField, "Adding A New Book. Enter Inputs For All Data Fields\n"+ tabulate(pandas.DataFrame(BOOK), headers='keys'), True)    
    writeToTextField(resultField, "Database:", False)      
    displayDatabase(resultField, BOOKS, False)

    # Assign Values and Save File if fully filled out
    if {} not in list(BOOK.values()):
        # Else add all inputs into database
        for key,valueDict in BOOK.items():
            BOOKS[key][entryID] = valueDict[entryID]
        saveExcel(resultField, filePath, "\nEntry Successfully Saved and Added!")
        resetBook()
    return True


# Checks if entryID exists in database
def findEntryID(resultField, entryID):
    if entryID not in list(BOOKS["ISBN"].keys()):
        writeToTextField(resultField, "Entry " + str(entryID) + " Not Found In Database.", True)
        displayDatabase(resultField, BOOKS, False)
        return False
    writeToTextField(resultField, "Entry " + str(entryID) + " Selected.\nSelect Data Type Then Submit Updated Value.", True)
    displayDatabase(resultField, BOOKS, False)
    return True

# Edits existing entry within database
def editEntry(resultField, entryID, dataTypeText, inputField, filePath):
    global BOOK
    global DEFAULT_FIELDS
    inputField = inputField.replace('-', '')

    if inputField == "":
        writeToTextField(resultField, "\nYou Cannot Enter Empty Inputs", True)  
        displayDatabase(resultField, BOOKS, False)
        return
    # Title and Author restriction - Letters Only
    elif dataTypeText == QUERYTYPES[1] and not isLettersOnly(inputField) or dataTypeText == QUERYTYPES[0] and not isLettersOnly(inputField):
        writeToTextField(resultField, "\n" + dataTypeText.capitalize() + " Cannot Contain Numerical Values and/or Special Characters", True)
        displayDatabase(resultField, BOOKS, False)
        return
    # ISBN restriction - Numbers Only
    elif dataTypeText == QUERYTYPES[2] and not isNumbers(inputField):
        writeToTextField(resultField, "\n" + dataTypeText.upper() + " Must Be Only Digits", True)
        displayDatabase(resultField, BOOKS, False)
        return
    # Purchased and Checked Out restriction - Integers only
    elif dataTypeText == QUERYTYPES[3] and not isInt(inputField) or dataTypeText == QUERYTYPES[4] and not isInt(inputField):
        writeToTextField(resultField, "\n" + dataTypeText.capitalize() + " Must Be An Integer Value", True) 
        displayDatabase(resultField, BOOKS, False)
        return
    # Price restriction - Float only
    elif dataTypeText == QUERYTYPES[5] and not isFloat(inputField):
        writeToTextField(resultField, "\n" + dataTypeText.capitalize() + " Must Be A Float Value", True)
        displayDatabase(resultField, BOOKS, False)
        return

    # Update Database Information
    BOOKS[dataTypeText][entryID] = inputField

    # Save Database 
    saveExcel(resultField, filePath, "Entry " + str(entryID) + " Successfully Updated and Saved!")

# Querys database by looking at its datatype and user input
def queryData(resultField, dataTypeText, inputField):
    queried_books = copy.deepcopy(DEFAULT_FIELDS)
    values = list(BOOKS[dataTypeText].values())
    values = [str(v).lower() for v in values]
    indexFound = []

    # Get index of books with queried input
    for i in range(len(values)):
        if inputField.lower() in str(values[i].lower()):
            indexFound.append(i)

    # Assign values to query and display
    for index in indexFound:
        for key, valueDict in BOOKS.items():
            queried_books[key][index] = valueDict[index]
    writeToTextField(resultField, "Results: ", True)
    displayDatabase(resultField, queried_books, False)
    writeToTextField(resultField, "Database:", False)
    displayDatabase(resultField, BOOKS, False)

# Get Book entryID To Remove
def getBookToRemove(resultField, inputField):
    values = list(BOOKS["ISBN"].values())
    values = [str(v).lower() for v in values]
    entryID = -1

    # Get index of books with queried input
    for i in range(len(values)):
        if inputField.lower() == str(values[i].lower()):
            print("FOUND", i)
            entryID = i
            #break
    if entryID != -1:
        writeToTextField(resultField, "Enter 'yes' To Confirm The Removal of Book " + str(entryID), True)  
    else:
        writeToTextField(resultField, "Could Not Find Book With ISBN " + inputField, True)  
    displayDatabase(resultField, BOOKS, False)
    return entryID

# Confirm ands removes data if yes was entered
def confirmRemove(resultField, inputField, entryID, filePath):
    if "yes" in str(inputField).lower():
        removeData(resultField, entryID, filePath)
    else:
        writeToTextField(resultField, "Canceled Removal of Book " + str(entryID), True)  
        displayDatabase(resultField, BOOKS, False)

# Remove data from database via entryID
def removeData(resultField, entryID, filePath):
    # Delete books via entryID list
    for key in BOOKS.keys():
        BOOKS[key].pop(entryID)

    saveExcel(resultField, filePath, "\nBook Successfully Removed From Database. Database Has Also Been Saved.")

# Saves database to excel. Creates an excel sheet if filepath isn't specified
def saveExcel(resultField, filePath, text = "\nDatabase Successfully Saved!"):
    if filePath == "":   
        try:
            pandas.DataFrame(BOOKS).to_excel(os.getcwd()+"\DefaultDataBase.xlsx", index=False)
        except:
            writeToTextField(resultField, "Issue Occured Saving/Adding Data. Please Make Sure Default DataFile Is Not Opened", True)
            return
    else:
        try:
            pandas.DataFrame(BOOKS).to_excel(filePath, index=False)
        except:
            writeToTextField(resultField, "Issue Occured Saving/Adding Data. Please Make Sure Specified DataFile Is Not Opened", True)
            return        
    writeToTextField(resultField, text, True)        
    displayDatabase(resultField, BOOKS,False)

# Displays database
def displayDatabase(resultField, database, value = True):
    writeToTextField(resultField, tabulate(pandas.DataFrame(database), headers='keys'), value)

# This will check to see if there are any digits inside the input and return a bool value
def isCharactersOnly(input):
    #while (any(char.isdigit() for char in input)): return False
    if (any(char.isdigit() for char in input)): return False
    return True

# This will make shure that only normal characters are inside and return bool values
def isLettersOnly(input):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ',',']
    if not isCharactersOnly(input):
        return False

    for char in input:
        letter = char.lower()
        if letter not in letters:
            return False
    return True

# This will check to make sure only digits were inputted and return a bool value
def isNumbers(input):
    if (any(not char.isdigit() for char in input)):
        return False
    return True

def isInt(input):
    try:
        int(input)
        return True
    except:
        return False

def isFloat(input):
    try:
        float(input)
        return True
    except:
        return False

def resetBook():
    global BOOK    
    BOOK.clear()
    BOOK = copy.deepcopy(DEFAULT_FIELDS)

def resetBooks():
    global BOOKS    
    BOOKS.clear()
    BOOKS = copy.deepcopy(DEFAULT_FIELDS)