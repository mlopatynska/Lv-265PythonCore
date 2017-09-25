from math import *

# 5
x = int(raw_input('Enter your x: '))
y = int(raw_input('Enter your y: '))
z = int(raw_input('Enter your z: '))

a = 2 * cos(x - pi / 6) / (1 / 2 + pow(sin(y), 2))
b = 1 + (pow(z, 2) / 3 + pow(z, 2) / 5)

print "The result of 'a' is %s and 'b' is %s" % (a, b)
