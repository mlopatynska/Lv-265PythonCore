# Quadratic equation
import math

a = input("Enter your 'a' value: ")
if a == 0:
    print "'a' can not be equal to 0"
else:
    b = input("Enter your 'b' value: ")
    c = input("Enter your 'c' value: ")

    d = b**2-4*a*c 

    if d < 0:
        print "This equation has no real solution"
    elif d == 0:
        x = (-b+math.sqrt(d))/(2*a)
        print "This equation has one solution: ", x
    else:
        x1 = (-b+math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2*a)
        print "This equation has two solutions: ", x1, " and", x2
