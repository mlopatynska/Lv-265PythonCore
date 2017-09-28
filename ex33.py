from math import exp, cos, sin

x1 = raw_input("X= ")
y1 = raw_input("Y= ")
z1 = raw_input("Z= ")
x = float(x1)
y = float(y1)
z = float(z1)

a = (1+y)*((x+(y/((x**2)+4)))/(exp(-x-2)+(1/(x**2+4))))
b = (1+cos(y-2))/(((x**4)/2)+(sin(z))**2)
print "a= %s" % (a)
print "b= %s" % (b)
