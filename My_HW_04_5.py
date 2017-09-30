k = input("Enter number from 1 to 365: ")
if 1 <= k <= 365:
    if k % 7 == 1:
        print "This is a Monday in year."
    elif k % 7 == 2:
        print "This is a Tuesday in year."
    elif k % 7 == 3:
        print "This is a Wednesday in year."
    elif k % 7 == 3:
        print "This is a Thursday in year."
    elif k % 7 == 3:
        print "This is a Friday in year."
    elif k % 7 == 3:
        print "This is a Saturday in year."
    else:
        print "This is a Sunday in year."
else:
    print "Input correct number!"
