a=3765
b=a//1000
c= a//100-(b*10)
d= a//10 -(b*100)-(c*10)
f= a- (b*1000)-(c*100)-(d*10)

k= b*c*d*f
m= (f*1000)+(d*100)+(c*10)+b
print "Zavdannya 1"
print k
print "Zavdannya 2"
print m 
print "Zavdannya 3"
x=list(str(a))
print x
z= sorted (x)
print z
x = ''.join(z) # ''
print x



