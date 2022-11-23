# Bryan Lor - Week 10 Lab Assignment

# Question 1
import math
def sphere_volume(r):
    return (4/3) * math.pi * r**3
#print(sphere_volume(5))

# Question 2
def print_range(start, end):    
    print(start)
    if start == end:
        return
    elif start > end:
        print_range(start - 1, end)
    elif start < end:
        print_range(start + 1, end)
# print_range(5,10)
# print()
# print_range(10,5)

# Question 3
def gcd(a, b):
    r = b % a
    if r == 0:
        return a
    return gcd(r, a)
#print(gcd(12, 8))
#print(gcd(20, 24))

# # Question 4
# import csv
# import json

# sales_data = []
# keys = ["Transaction Date", "Product", "Price", "Payment Type", "Name", "City", "State", "Country"]

# with open("SalesJan2009.csv", newline="") as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         rowDict = {}
#         for i in range(len(row)):
#             rowDict[keys[i]] = row[i]
#         sales_data.append(rowDict)
# json_object = json.dumps(sales_data)

# Question 5
import csv
with open("SalesJan2009.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print("Data:", row)
        filterA = [x for x in row if "a" in x.lower()]
        filterMaster = [x for x in row if "master" in x.lower()]
        print("Filter 'A':", filterA)
        print("Filter 'Master':", filterMaster)
        print()
