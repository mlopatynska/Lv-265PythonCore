from math import sqrt

print"Enter three values of the sides of the triangle"
a = float(input("Enter value of first side: "))
b = float(input("Enter value of second side: "))
c = float(input("Enter value of third side: "))
if a + b > c and b + c > a and c + a > b:
    p = a + b + c
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print "Congratulation! We built the triangle with perimeter {} meters and area of {} square meters.".format(p, s)
else:
    print "We can not build triangle because value of sides are not valid."
