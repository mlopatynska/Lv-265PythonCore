k = int(raw_input("Enter k from 1 to 365: "))

n = k % 7

if n == 1:
    print "Monday"
elif n == 2:
    print "Tuesday"
elif day == 3:
    print "Wednesday"
elif day == 4:
    print "Thursday"
elif day == 5:
    print "Friday"
elif day == 6:
    print "Saturday"
else:
    print "Sunday"
