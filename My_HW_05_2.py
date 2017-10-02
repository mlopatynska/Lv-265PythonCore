num = input("Enter number: ")
if num > 1:
    for elem in range(2, num):
        if num % elem == 0:
            print "This is a not prime number"
            break
    else:
        print "This is a prime number."
else:
    print "Enter only number more than 1!"
