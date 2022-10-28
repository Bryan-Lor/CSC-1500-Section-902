#Bryan Lor - Week 8 Lab Assignment

# Question 1
n = int(input("Enter a number: "))
n = (((n + 2) * 3) - 6) / 3
print(n)

# Question 2
my_var1 = 7.0
my_var2 = 5
print("Group one:",my_var1 % my_var2)

x = 4
y = 5
print("Group Two:", x//y)

print("Group Three:",30-2**2+8//3**2*10)

# Question 3
while True:
    x = input("Give me an input: ")
    try: 
        int(x)
        print("No issue with turning it into an integer:", x)
    except:
        print("Can't turn x into an integer")
    try: 
        float(x)
        print("No issue with turning it into an float:", x)
    except:
        print("Can't turn x into a float")
    print()

# Question 4
a = 2**2**3
b = 2**(2**3)
c = (2**2)**3

print("a:", a)
print("b:", b)
print("c:", c)

# Questions 5
import random

treasure = ["gold coin", "pirate hat", "hook", "wooden leg", "gold skull", "gold medallion", "ripped rags",
"black diamond", "pearl necklaces", "eye patch", "captains jacket", "green emerald", "bottle of rum", "old map"]
stash = []
items = ""
stashMax = 5

for i in range(len(treasure)):
    items += treasure[i] + ", "
print("Treasure Chest:","\n" + items)

while len(stash) <= stashMax :
    print("\nStash Capacity:", stashMax, "- Available Space:", stashMax - len(stash) )
    if len(stash) >= 1:
        print(stash)
    input("Enter Anything To Randomly Grab An Item: ")
    itemPicked = random.choice(treasure)
    stash.append(itemPicked)
    treasure.remove(itemPicked)
    if stashMax - len(stash) <= 0:
        break
print("\nStash Reached Maximum Limit, Cannot Grab Anymore Items!\n", stash)

# Question 6
import random

def generatePassword(length):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!', '#',"$", "&", "%"]

    password = ""
    while len(password) < length:
        x = random.randint(0,2)
        match(x):
            case 0:
                password += random.choice(letters)
            case 1:
                password += random.choice(numbers)
            case 2:
                password += random.choice(symbols)
    return password

passwords = []
l = int(input("Enter the maximum length of the passwords: "))
x = int(input("Enter the amount of passwords you want to generate: "))
i = 1
while i <= x:
    password = generatePassword(l)
    if password not in passwords:
        passwords.append(password)
        i += 1

print("Passwords Generated:")
for i in range(len(passwords)):
    print(i+1, passwords[i])

# Question 7
processAvg = 16.507
avgRange = 0.561
std = 11.768
upperLimit = 10
lowerLimit = 2

cpk = min((upperLimit - processAvg)/(3 * std), (processAvg-lowerLimit)/(3 * std))
print(cpk)

# Question 8
def checkPrime(num):
    x = 0
    if num < 1:
        return False   

    for i in range(1, num + 1):
        if (num % i) == 0:
            x += 1
            if x > 2:
                return False
    return True

limit = 100
primeNumbers = []
for currentNumber in range(2, limit):
    if (checkPrime(currentNumber)) == True:
        primeNumbers.append(currentNumber)
print(primeNumbers)

# Question 9
x = input("Enter the bill and tip percentage: ").split()
bill, tipPercent = x
tip = int(bill) * (int(tipPercent) / 100)
print("Tip Amount:", "$" + str(tip))