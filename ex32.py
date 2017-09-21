from math import fabs, tan, exp

x1 = raw_input("X= ")
y1 = raw_input("Y= ")
z1 = raw_input("Z= ")
x = int(x1)
y = int(y1)
z = int(z1)

a = (3+exp(y-1))/(1+(x**2)*fabs(y-tan(z)))
b = 1+fabs(y-x)+((y-x)*2)/2+((fabs(y-x))**3)/3
print "a= %s" % (a)
print "b= %s" % (b)