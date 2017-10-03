n=int(raw_input("Number:"))
i=2
j=0
while i**2 <= n and j != 1:
       if n%i == 0:
            j=1
       i+=1
if j == 1:
     print ("That's a prime number)")
else:
    print ("That's a composite number)")
