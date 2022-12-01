#Bryan Lor - Week 11 Lab Assignment
import math


# Question 1
def AreaofCirle(**args):
    return (math.pi * list(args.values())[0] ** 2)
circle = AreaofCirle(radius = 5)
#print(circle)

# Question 2
def VolumeofCube(**args):
    return (list(args.values())[0] ** 3)
cube = VolumeofCube(length = 729)
#print(cube)

# Question 3
def PythagoreanTheorem(**args):
    return (list(args.values())[0] ** 2) + (list(args.values())[1] ** 2)
triangle = math.sqrt(PythagoreanTheorem(a = 18, b = 10))
#print(triangle)

# Question 4
def function(**args):
    numerator = (args['a'] + args['b']) ** 3 - args['c']
    denominator = args['d'] + (args['e'] - args['f']) * (args['g'] - args['h']) ** (-0.4)
    print("numerator", numerator)
    print("denominator", denominator)
    return math.sqrt(numerator/denominator)
#print(function(a = 4.172, b = 9.131844, c = 18, d = -3.5, e = 11.2,f = 4.6, g = 7, h = 2.91683))

# Question 5
def f(a, b = 4, c = 5):
    print(a,b,c)
f(1, 2)

def f(a, b, c = 5):
    print(a,b,c)
f(1, c=3, b=2)