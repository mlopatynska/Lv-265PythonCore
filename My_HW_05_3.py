n = input("Enter number: ")
i = 0
f1 = 0
f2 = 1
while i < n:
    f = f1 + f2
    f1 = f2
    f2 = f
    i +=1
    print "Number -{}- of fibonacci is: {} ".format(i,f2)
