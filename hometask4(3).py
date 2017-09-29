a=float(raw_input('Enter a:'))
b=float(raw_input('Enter b:'))
c=float(raw_input('Enter c:'))
import math
D=b**2-4*a*c
print "D=%f"%D
if D>=0:
    x1=(-b+math.sqrt(D))/2*a
    x2=(-b-math.sqrt(D))/2*a
    print "The roots of the equation:"
    print "X1=%f"%x1
    print "X2=%f"%x2
else:
    print "This equation doesn't have float roots."
    
