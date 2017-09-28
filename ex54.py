from math import sqrt

a = float(raw_input("Enter a: "))
b = float(raw_input("Enter b: "))
c = float(raw_input("Enter c: "))

p = (a + b + c)
s = sqrt((p/2) * (p/2 - a) * (p/2 - b) * (p/2 - c))

if ((a+b)>c and (a+c)>b and (b+c)>a):
     print "It's possible to create a triangle. Perimetr: {} \nSquare: {}".format(p, s)
else:
     print "Impossible to create triangle"
