
from math import * 
x = int(raw_input('Enter x:'))
y = int(raw_input('Enter y:'))
z = int(raw_input('Enter z:'))

#1
a = (sqrt(fabs(x-1))-(fabs(y)**(1/3.0)))/(1+(x**2/2)+(y**2/4))
b = x*(atan(z) + e**(-(x+3)))
print ("In exercise 1:")
print ("a = " ),a
print ( "b = "),b


#2
a = (3+e**(y-1))/(1+x**2*fabs(y-tan(z)))
b = 1+fabs(y-x)+(((y-x)**2)/2)+((fabs(y-x)**3)/3)
print ("In exercise 2:")
print ("a = " ),a
print ( "b = "),b 


#3
a = (1+y)*((x+y/(x*2+4))/(e**(-x-2)+1/(x**2+a)))
b = (1+cos(y-2))/(x**4/2+sin(z)**2)
print ("In exercise 3:")
print ("a = " ),a
print ( "b = "),b


#4
a = y + x /(y**2+fabs(x**2/y+x**3/3))
b = (1+tan(z/2)**2)
print ("In exercise 4:")
print ("a = " ),a
print ( "b = "),b


#5
a = 2*cos(x-pi/6)/(1/2+sin(y)**2)
b = 1+z**2/(3+z**2/5)
print ("In exercise 5:")
print ("a = " ),a
print ( "b = "),b


#6
a = ((1+sin(x+y)**2)/(2+fabs(x-2*x/(1+x**2*y**2))))+x
b = cos(atan(1/z))**2
print ("In exercise 6:")
print ("a = " ),a
print ( "b = "),b


#7
a = log(fabs((y-sqrt(fabs(x)))*(x-y/(z+x**2/4))))
b = x-((x**2/factorial(3))+(x**5/factorial(5)))
print ("In exercise 7:")
print ("a = " ),a
print ( "b = "),b 
