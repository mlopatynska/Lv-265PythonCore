myNumber = int(raw_input("Enter a number: "))

for i in range(2,myNumber):
    if myNumber%i != 0 :
        prime = True
print prime
if prime:
    print "{} is a prime number".format(myNumber)
else:
    print "{} is NOT a prime number".format(myNumber)






        #print "{} is a prime number".format(myNumber)
    #else:
     #   print "{} is not a prime number".format(myNumber)
