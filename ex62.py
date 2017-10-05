def prime_check(a):
a = int(raw_input("Enter A>1:"))

for k in range(2, a):
if a%k == 0:
print ("{} is a COMPOSITE number").format(a)
break

else:
print ("{} is a PRIME number").format(a)

prime_check(17)
