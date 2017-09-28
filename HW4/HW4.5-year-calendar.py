daynumber = float(raw_input("Enter, please, the day's number: "))
if daynumber > 0 and daynumber < 366 :
    if daynumber %7 == 0 :
        print "It\'s Sunday"
    elif daynumber %7 == 1:
        print "It\'s Monday"
    elif daynumber %7 == 2:
        print "It\'s Tuesday"
    elif daynumber %7 == 3:
        print "It\'s Wednesday"
    elif daynumber %7 == 4:
        print "It\'s Thursday"
    elif daynumber %7 == 5:
        print "It\'s Friday"
    elif daynumber %7 == 6:
        print "It\'s Saturday"
else:
    print "Error"
