d = input("Please enter your number: ")

for i in range(2, d):
    if d%i == 0:
        print "The number you indicated is composite: {}".format(d)
        break

else:
    print "The number you indicated is prime: {}".format(d)
        
