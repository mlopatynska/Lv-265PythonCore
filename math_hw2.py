from math import *

# 4
x = int(raw_input('Enter your x: '))
y = int(raw_input('Enter your y: '))
z = int(raw_input('Enter your z: '))


a = y + (x/pow(y, 2)+fabs(pow(x, 2)/y+pow(x, 3)/3))
b = (1 + pow(tan(z/2), 2))

print "The result of 'a' is %s and 'b' is %s" % (a, b)
