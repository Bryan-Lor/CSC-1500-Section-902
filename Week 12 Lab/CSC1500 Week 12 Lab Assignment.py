#Bryan Lor - Week 12 Lab Assignment

# Question 1 - Create the list with data
data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
    ]
#print(data)

# Question 2, 3, and 4 - Format list to dictionary database without duplicates
employee = {}
employeeDatabase = {}

# Add to employee dictionary based on object type of info. 
# This will assign it to its corresponding category.
def addToDatabase(info):
    if type(info) == bool: # Bool value
        employee["Bool"] = info
    elif type(info) == int: # Employee Information
        employee["ID"] = info
    elif type(info) == str: # Employee Name
        employee["Name"] = info
    elif type(info) == float: # Employee Wage and Total Wage
        employee["Wage"] = info
        employee["Total Wage"] = info * 1.3
    else:
        print("Error: Unspecified instructions to add data type " + str(type(info)) + " to database.")

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
        addToDatabase(info)
    else:
        # Add to employee dictionary to fill it out
        addToDatabase(info)
        counter += 1
print("EmployeeDatabase:\n", employeeDatabase)
print()


# Question 5 - Find underpaid salaries between 28.15 and 30.65

# # Original implimentation to get underpaid salaries via a FOR loop
# underpaidSalaries = []
# for personID in employeeDatabase:
#     if employeeDatabase[personID]["Total Wage"] > 28.15 and employeeDatabase[personID]["Total Wage"] < 30.65:
#         personDict = {}
#         personDict[personID] = employeeDatabase[personID]
#         underpaidSalaries.append(personDict)
#print("Underpaid Salaries:\n", list(getUnderpaidSalaries))

# Generator implimentation to get underpaid salaries and return a BOOLEAN value
getUnderpaidSalaries = (employeeDatabase[person]["Total Wage"] > 28.15 and employeeDatabase[person]["Total Wage"] < 30.65 for person in employeeDatabase)
underpaidSalaries = []
for index, value in enumerate(getUnderpaidSalaries):
    if value:
        keys = list(employeeDatabase.keys())
        person = {}
        person[keys[index]] = employeeDatabase[keys[index]]
        underpaidSalaries.append(person)
        underpaidSalaries.append(employeeDatabase[keys[index]])
print("Underpaid Salaries:\n", underpaidSalaries)
print()

# Question 6 - Calculate a raise for all salaries in database
companyRaises = []
for personID in employeeDatabase:    
    person = {}
    person[personID] = employeeDatabase[personID]
    if employeeDatabase[personID]["Wage"] > 22 and employeeDatabase[personID]["Wage"] < 24:
        # 5% Raise
        person[personID]["Wage"] *= 1.05
    elif employeeDatabase[personID]["Wage"] > 24 and employeeDatabase[personID]["Wage"] < 26:
        # 4% Raise
        person[personID]["Wage"] *= 1.04
    elif employeeDatabase[personID]["Wage"] > 26 and employeeDatabase[personID]["Wage"] < 28:
        # 3% Raise
        person[personID]["Wage"] *= 1.03
    else:
        # 2% Standard Raise
        person[personID]["Wage"] *= 1.02        
    companyRaises.append(person)
print("Company Raises:\n", companyRaises)