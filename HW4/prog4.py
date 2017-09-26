import math
print "enter a"
a= float ( input())
print "enter b"
b= float ( input())
print "enter c"
c= float ( input())
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
if (a+b > c) and (b+c > a) and (a+c > b) and (a>0) and(b>0) and (c>0) :
     print( "P=", a+b+c , "S=", s );

else:
     print ("Not exist")