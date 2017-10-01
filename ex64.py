a = int(raw_input("Enter A:"))

s=0
while a>0:
a_ost=a%10
s = s+a_ost**3
a = a//10

else
print ("The sum of the cubes of digits of number{}: {}").format(a, s)
