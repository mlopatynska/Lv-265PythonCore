from math import fabs, tan

x1 = raw_input("X= ")
y1 = raw_input("Y= ")
z1 = raw_input("Z= ")
x = int(x1)
y = int(y1)
z = int(z1)

a = y+(x/((y**2)+fabs((x**2)/(y+(x**3)/3))))
b = 1+(tan(z/2))**2
print "a= %s" % (a)
print "b= %s" % (b)