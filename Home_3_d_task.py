from math import *

print "Hello!"
print "Input below only figures. Lets start."
x = input("Input figure x: ")
y = input("Input figure y: ")
z = input("Input figure z: ")

a = y + (x / (pow(y, 2) + fabs(pow(x, 2) / (y + pow(x, 3) / 3))))
b = 1 + pow(tan(z / 2), 2)
print "a = {} \nb = {}".format(a,b)