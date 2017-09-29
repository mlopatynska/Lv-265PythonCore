a=float(raw_input("The side a:"))
b=float(raw_input("The side b:"))
c=float(raw_input("The side c:"))
if a+b>c and a+c>b and b+c>a:
    print ("We can make a triangle)")
    P=a+b+c
    print "The perimeter is %f "%P
    p=P/2
    import math
    S=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print "The area is %f "%S
else:
    print ("We can't make a triangle(")
