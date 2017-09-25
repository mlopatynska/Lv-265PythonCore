from math import *

print "Hello!"
print "Input below only figures. Lets start."
x = input("Input figure x: ")
y = input("Input figure y: ")
z = input("Input figure z: ")

a = (2 * cos(x - pi / 6)) / ( 1 / 2 + pow(sin(y), 2))
b = 1 + pow(z, 2) / (3 + pow(z, 2) / 5)
print "a = {} \nb = {}".format(a,b)