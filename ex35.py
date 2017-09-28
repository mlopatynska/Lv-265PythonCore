from math import pi, cos, sin

x1 = raw_input("X= ")
y1 = raw_input("Y= ")
z1 = raw_input("Z= ")
x = float(x1)
y = float(y1)
z = float(z1)

a = (2*cos(x-pi/6))/(0.5+(sin(y))**2)
b = 1+(z**2)/(3+(z**2)/5)
print "a= %s" % (a)
print "b= %s" % (b)