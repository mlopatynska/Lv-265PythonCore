k = int(raw_input("Enter day number from 1 to 365: "))

n = k % 7

if n == 1:
    print "It's Monday"
elif n == 2:
    print "It's Tuesday"
elif n == 3:
    print "It's Wednesday"
elif n == 4:
    print "It's Thursday"
elif n == 5:
    print "It's Friday"
elif n == 6:
    print "It's Saturday"
else:
    print "It's Sunday"
