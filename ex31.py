from math import sqrt, fabs, pow, atan, exp

x1 = raw_input("X= ")
y1 = raw_input("Y= ")
z1 = raw_input("Z= ")
x = int(x1)
y = int(y1)
z = int(z1)

a = (sqrt(fabs(x-1))-pow(fabs(y),(1/3))) / (1+(x**2)/2+(y**2)/4)
b = x*(atan(z)+exp(-(x+3)))
print "a= %s" % (a)
print "b= %s" % (b)