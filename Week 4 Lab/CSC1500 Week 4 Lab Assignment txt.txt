#Bryan Lor - Week 4 Lab Assignment

#Question 1
print("\033[1;37;40m" + "Please enter a string: ")
string = input("\033[1;31;40m")
print("\033[1;37;40m" + "You Entered " + string + " and its type is " + str(type(string)))
print("\033[1;37;40m" + "Please enter an integer: ")
integer = input("\033[1;31;40m")
print("\033[1;37;40m" + "You Entered " + integer + " and its type is " + str(type(integer)))

#Question 2
print("""\"Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky.\"
\"Twinkle, twinkle, little star, 
	How I wonder what you are\"
""")

#Question 3
r = input("r = ")
area = float(r) * float(r) * 3.141592653
print("Area = " + str(area))

#Question 4
vowels = ["a", "e", "i", "o", "u"]
x = "tet"
isVowel = False
while True:
    while len(x) > 1:
        x = input("Give me a letter: ")
    for element in vowels:
        if x == element:
            isVowel = True
    if isVowel == True:
        print("It is a vowel!")
        x = "tet"
    else:
        print("Not a vowel.")
        x = "tet"

#Question 5
l = [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000, 14641, 20736, 28561, 38416, 50625, 65536, 83521, 104976]
print(l)

#Question 6 
import random
Slots = ["Green 00", "Green 0", 
    "Red 1", "Red 27", "Red 25", "Red 12", "Red 19", "Red 18", "Red 21",
    "Red 16", "Red 23", "Red 14", "Red 9", "Red 30", "Red 7", "Red 32",
    "Red 5", "Red 34", "Red 3", "Red 36",
    "Black 10", "Black 29", "Black 8", "Black 31", "Black 6", "Black 33",
    "Black 4", "Black 35", "Black 2", "Black 28", "Black 26", "Black 11",
    "Black 20", "Black 17", "Black 22", "Black 15", "Black 24", "Black 13"]
Log = []
print("Roulette Wheel!\n--------------")
while True:
    x = input("\nEnter Anything To Roll (Type 'Log' To Show Log): ")
    if("log" in x.lower()):
        print("\nLog: " + str(Log))
    else:
        roll = random.choice(Slots)
        Log.append(roll)
        print("\nYou Landed On "+ roll + "!")

#Question 7
DinnerGuests = []
InvitationDate = []
smallTagLength = 9
BigTags = []
SmallTags = []
totalGuests = 5

print("There are " + str(totalGuests) + " guests attending this dinner.\n")
i = 1
while i <= totalGuests:
    name = input(str(i) + ") Enter The Guests' First and Last Name: ")
    DinnerGuests.append(name)
    date = input("Enter The Invitation Date For " + name + ": ")
    InvitationDate.append(date)
    print()
    i = i + 1


for person in DinnerGuests:
    print(str(person) + " - Invited " + str(InvitationDate[DinnerGuests.index(person)]))
    if len(person) > smallTagLength:
        BigTags.append(person)
    else:
        SmallTags.append(person)

print("\nBig Tags: " + str(BigTags))
print("Small Tags: " + str(SmallTags))
