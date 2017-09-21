from math import *

print "Hello!"
print "Input below only figures. Lets start."
x = input("Input figure x: ")
y = input("Input figure y: ")
z = input("Input figure z: ")
e = input("Input figure e: ")

a = (3 + pow(e, y - 1)) / 1 + pow(x, 2) * fabs((y - tan(z)))
b = 1 + fabs(y - x) + pow((y - x), 2) / 2 + pow(fabs(y - x), 3) / 3
print "a = {} \nb = {}".format(a, b)
