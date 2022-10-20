#Bryan  Lor - Week 7 Lab Assignment

# Work Ticket 1
def makeDictionary(list1, list2):
    dictionary = {}
    for i in range(len(list1)):
        dictionary[list1[i]] = list2[i]
    return dictionary

names = ['joe', 'tom', 'barb', 'sue', 'sally']
scores = [10, 23, 13, 18, 12]
scoreDict = makeDictionary(names, scores)
#print(scoreDict)

# # Work Ticket 2
# while True:
#     s = "Students: "
#     for names in scoreDict:
#         s += names + ", "
#     print(s)
#     x = input("Who's score whould you like to see? ")
#     if x in scoreDict:
#         print(scoreDict.get(x))
#     else:
#         print("No student with the name '" + x + "' was found. Try again.\n")

# # Work Ticket 3
# while True:
#     s = "Student Grades-------------------\n"
#     for names in scoreDict:
#         s += names.capitalize() + " - " + str(scoreDict[names]) + "\n"
#     print(s)
#     x = input("1. Add Student\n0. Quit\nEnter 0 or 1: ")
#     if x == "0":
#         break
#     elif x == "1":
#         name = input("Enter the student's name: ")
#         grade = input("Enter the student's grade: ")
#         if name in scoreDict:
#             print("That student is already in the dictionary.\n")
#         else:
#             scoreDict[name] = int(grade)
#             print()
#     else:
#         print("Must enter 0 or 1\n")

# # Work Ticket 4
# sortedScoreList = sorted(scoreDict.values())
# print(sortedScoreList)

# Work Ticket 5
def printStudents():
    s = "\nStudent Grades-------------------\n"
    for names in scoreDict:
        s += names.capitalize() + " - " + str(scoreDict[names]) + "\n"
    print(s)

def addStudent():
    print("    ==== Add Student ====")
    name = input("    Enter the student's name: ").lower()
    grade = int(input("    Enter the student's grade: "))
    if name in scoreDict:
        print("    That student is already in the dictionary.\n")
    else:
        scoreDict[name] = grade
        print()

def deleteStudent():
    print("    ==== Delete Student ====")
    name = input("    Enter the name of the student to delete: ")
    scoreDict.pop(name.lower())
    print()

def queryStudent():
    print("    ==== Query Student ====")
    x = input("    Filter by letters/name: ")
    print({k:v for (k,v) in scoreDict.items() if x in k})
    print()

while True:
    x = input("1. Show Students\n2. Add Student\n3. Delete Student\n4. Query Student"
    "\n0. Quit\nEnter [0-4]: ")
    match x:
        case "0":
            break
        case "1":
            printStudents()
        case "2":
            addStudent()
        case "3":
            deleteStudent()
        case "4":
            queryStudent()
        case _:
            print("Must enter [0-5]!\n")