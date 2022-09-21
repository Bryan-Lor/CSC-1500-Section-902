#Bryan Lor - CSC1500 Week 3 Lab Assignment
#Time taken (X:XX) is in minutes and seconds

#Work Ticket 1 - String Formatting (6:55) -------------------------
#1) -------
print('"Hey There"')
#2) -------
print("How's everything goin'?")
#3) -------
print(""" I am a multi-lined 
    string who takes up 
        multiple lines of code.""")
#4) -------
print("I am also",
 "multi-lined but",
  "I print in one go.")

#Work Ticket 2 - String Functions (4:00) -------------------------
#1) -------
s = "I am a string of a certain length"
print(len(s))
#2) -------
s1 = "I am a"
s2 = "part of you"
s = s1 + s2
print (s)
#3) -------
print(s1 + " " + s2)
#4) -------
s = "bazinga"
print(s[2:6])

#Work Ticket 3 - String Methods (5:20) -------------------------
#1) -------
strings = ["Animals", "Badger", "Honey Bee", "Honey Badger"]
for string in strings:
    print (string.lower())
#2) -------
for string in strings:
    print (string.upper())
#3) -------
string1 = " Fillet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "
print(string1.replace(" ", ""))
print(string2.replace(" ", ""))
print(string1.replace(" ", ""))
#4) -------
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = "bEautiful"
print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))

#Work Ticket 4 - Input Methods (8:00) -------------------------
#1) -------
string = "4"
number = int(string)
print(number * 5)
#2) -------
string = "4.65"
f = float(string)
print(f * 2.4)
#3) -------
string = "Number :"
number = 521
print(string + str(number))
#4) -------
n1 = input("Give me a number: ")
n2 = input("Give me another number: ")
print("The product of " + n1 + " and " + n2 + " is " + str(float(n1) * float(n2)))
#5) -------
string = "This is a message that contains a few words that I wrote"
print(string.find("contains"))