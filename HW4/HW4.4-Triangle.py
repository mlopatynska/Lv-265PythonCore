length1 = int(raw_input("Enter the first side's length: "))
length2 = int(raw_input("Enter the second side's length: "))
length3 = int(raw_input("Enter the third side's length: "))
from math import *
maxLength = max(length1,length2, length3)
perimeter = length1+length2+length3
if maxLength < (perimeter - maxLength):
    print "Perimeter: ", perimeter
    S = sqrt(perimeter*(perimeter-length1)*(perimeter-length2)*(perimeter-length3))
    print "Area: ", S
else:
    print "You can't built triangle with such sides"
