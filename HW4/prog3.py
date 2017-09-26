import math
print "enter a"
a= float ( input())
print "enter b"
b= float ( input())
print "enter c"
c= float ( input())
d=b**2-4*a*c
if (d>0)  :
     x1=(-b+math.sqrt(d))/(2*a)
     x2 = (-b - math.sqrt(d)) / (2 * a)
     print( "X1=", x1  , "X2", x2 );
elif d==0 :
     x=-b/(2*a)
     print ("X=", x)
else :
     print ("Not exist")