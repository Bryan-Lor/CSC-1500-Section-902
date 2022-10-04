#Bryan Lor - Week 5 Lab Assignment

import math

#Question 1 --------------------
firstName = "bryan"
lastName = "LOR"
firstName = firstName.lower()
lastName = lastName.upper()
print("\nHello, " + firstName + " " + lastName)

print("\n")

fullName = firstName + " " + lastName
print(fullName[6:])
fullName = fullName[:6] + "Walsh College Student"
print(fullName)

print("""\x1B[3m \"Start by doing what's necessary; then do what's
    possible; and suddenly you are doing the impossible
    - Francis of Assisi\"\x1B[0m\n""")

decOne = 5.2
decTwo = 10.8

addition = decOne + decTwo
subtraction = decOne - decTwo
multiplication = decOne * decTwo
division = decOne / decTwo

print(str(round(decOne, 2)) + " plus " + str(round(decTwo, 2)) + " equals " + str(round(addition, 2)))
print(str(round(decOne, 2)) + " minus " + str(round(decTwo, 2)) + " equals " + str(round(subtraction, 2)))
print(str(round(decOne, 2)) + " times " + str(round(decTwo, 2)) + " equals " + str(round(multiplication, 2)))
print(str(round(decOne, 2)) + " divided by " + str(round(decTwo, 2)) + " equals " + str(round(division, 2)) + "\n")

sqrRoot = round(math.sqrt(multiplication), 2)
print("The square root of " + str(round(multiplication, 2)) + " equals " + str(round(sqrRoot, 2)) + "\n")

currentMonth = "October"
currentDay = 3

print("     Today is " + str(currentDay) + " of the month of " + currentMonth + ".")