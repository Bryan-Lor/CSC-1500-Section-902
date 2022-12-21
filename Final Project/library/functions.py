# Bryan Lor - Functions used within main program
from tabulate import tabulate
import pandas as pd
import itertools as itl
import tkinter as tk

# Reads excel file and returns data
def importFile(fileName="data.xlsx"):
    df = pd.read_excel(fileName, sheet_name=0, na_filter=False)
    values = df.values.tolist()
    data = list(filter(lambda n: n != "", itl.chain.from_iterable(values)))
    return data

# Prints out the main employee database
def printEmployeeDatabase(resultField, database, header="Database", clear=False):
    writeToTextField(resultField, header, clear)
    for key in database:
        writeToTextField(resultField, "========================================")
        keys = ["Employee ID", key]
        writeToTextField(resultField, tabulate(database[key].items(), headers=keys))

# Prints out any other database that has been modified
def printDatabase(resultField, database, header="Database", clear=False):
    writeToTextField(resultField, header, clear)
    for person in database:
        writeToTextField(resultField, "========================================")
        keys = list(person.keys())
        keys.insert(0, "Employee ID")
        personDict = person[keys[1]]
        writeToTextField(resultField, tabulate(personDict.items(), headers=keys))

# Writes to text field widget
def writeToTextField(field, text, clear=False):
    field.config(state="normal")
    if clear: field.delete("0.0","end")
    field.insert(tk.INSERT, text + "\n\n")
    field.config(state="disabled")

# Saves database to excel. Creates an excel sheet if filepath isn't specified
def saveExcel(data, initialDir, name = "DefaultDataBase"):
    try:
        pd.DataFrame(data).to_excel(initialDir+"\\\\"+ name + ".xlsx", index=False)
        return True
    except:
        return False

# Add to employee dictionary based on object type of info. 
# This will assign it to its corresponding category.
def addToDatabase(info, employee):
    objType = type(info)
    if objType == bool: # Bool value
        employee["Bool"] = info
    elif objType == int: # Employee Information
        employee["ID"] = info
    elif objType == str: # Employee Name
        employee["Name"] = info
    elif objType == float: # Employee Wage and Total Wage
        employee["Wage"] = round(info, 2)
        employee["Total Wage"] = round(info * 1.3, 2)
    else:
        print("Error: Unspecified instructions to add data type " + str(objType) + " to database.")


# Creates the database from the file information
def importDatabase(data):
    employee = {}
    employeeDatabase = {}
    counter = 1
    for info in data:
        if type(info) is not bool and counter > 3:
            # Add created employee dictionary to database assigned with their ID
            # then reset employee for next iterations
            id = employee["ID"]
            del employee["ID"]
            employeeDatabase[id] = employee
            counter = 2
            employee = {}
            addToDatabase(info, employee)
        else:
            # Add to employee dictionary to fill it out
            addToDatabase(info, employee)
            counter += 1
    return employeeDatabase

# Converts list of dictionaries into one single dictionary to save and export
def createSaveFile(listData):
    if type(listData) != list:
        return
    saveData = {}
    for data in listData:
        saveData.update(data)
    return saveData

# Generator implimentation to get underpaid salaries and return a BOOLEAN value
def getUnderpaidSalaries(database):
    underpaidSalariesGen = (database[person]["Total Wage"] > 28.15 and database[person]["Total Wage"] < 30.65 for person in database)
    underpaidSalaries = []
    for index, value in enumerate(underpaidSalariesGen):
        if value:
            keys = list(database.keys())
            person = {}
            person[keys[index]] = database[keys[index]]
            underpaidSalaries.append(person)
    return underpaidSalaries

# Calculate a raise for all salaries in database
def getSalaryRaises(employeeDatabase):
    companyRaises = []
    for personID in employeeDatabase:    
        person = {}
        person[personID] = employeeDatabase[personID]
        wage = person[personID]["Wage"]
        if employeeDatabase[personID]["Wage"] > 22 and employeeDatabase[personID]["Wage"] < 24:
            person[personID]["Wage"] = round(wage * 1.05, 2) # 5% Raise

        elif employeeDatabase[personID]["Wage"] > 24 and employeeDatabase[personID]["Wage"] < 26:
            person[personID]["Wage"] = round(wage * 1.04, 2) # 4% Raise

        elif employeeDatabase[personID]["Wage"] > 26 and employeeDatabase[personID]["Wage"] < 28:
            person[personID]["Wage"] = round(wage * 1.03, 2) # 3% Raise
            
        else:
            person[personID]["Wage"] = round(wage * 1.02, 2) # 2% Standard Raise 
        companyRaises.append(person)
    return companyRaises

