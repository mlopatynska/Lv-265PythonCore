from math import *

# 6
x = int(raw_input('Enter your x: '))
y = int(raw_input('Enter your y: '))
z = int(raw_input('Enter your z: '))

a = ((1 + pow(sin(x+y), 2)) / (2 + fabs(x - 2*x/(1+pow(x, 2)*pow(y, 2))))) + x
b = pow(cos(atan(1/z)), 2)

print "The result of 'a' is %s and 'b' is %s" % (a, b)
