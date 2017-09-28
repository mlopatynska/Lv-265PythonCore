a = float(raw_input("Please, enter a:"))
b = float(raw_input("Please, enter b:"))
c = float(raw_input("Please, enter c:"))
from math import *
if (b**2 - 4*a*c) >= 0:
    D = sqrt(b**2 - 4*a*c)
    x1= (-b+D)/(2*a)
    x2= (-b-D)/(2*a)
    print "Discriminant: ", D
    print "X1:", x1
    print "X2", x2
else:
    print "Have no real roots"
