from math import cos, sin, atan, fabs

x1 = raw_input("X= ")
y1 = raw_input("Y= ")
z1 = raw_input("Z= ")
x = float(x1)
y = float(y1)
z = float(z1)

a = (1+(sin(x+y))**2)/(2+fabs(x-(2*x)/(1+x*x*y*y)))
b = (cos(atan(1/z)))**2
print "a= %s" % (a)
print "b= %s" % (b)