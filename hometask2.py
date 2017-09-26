x=float(raw_input("Число x="))
print x
y=float(raw_input("Число y="))
print y
z=float(raw_input("Число z="))
print z
import math
a1=(math.sqrt(abs(x-1))+pow(abs(y),1/3))/(1+(pow(x,2)/2)+(pow(y,2)/4))
print a1
b1=x*(math.atan(z)+pow(2.71828,(-x-3)))
print b1
a2=y+(x/pow(y,2)+abs(pow(x,2)/(y+pow(x,3)/3)))
print a2
b2=1+pow(math.tan(z/2),2)
print b2
a3=2*math.cos(x-3.14/6)/(0.5+pow(math.sin(y),2))
print a3
b3=1+pow(z,2)/(3+(pow(z,2)/5))
print b3
