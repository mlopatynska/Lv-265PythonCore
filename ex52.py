day = int(raw_input("Enter day: "))
month = int(raw_input("Enter month: "))
year = int(raw_input("Enter year: "))

if day > 31:
    print "Date is NOT CORRECT"
elif month < 1 or month > 12:
    print "Date is NOT CORRECT"
    elif (((month == 2)or (month == 4) or (month == 6) or (month == 9) or (month == 11)) and (day == 31)) or (month == 2 and day == 30) or ((year % 4 == 0 and month == 2 and day == 29)):
        print "Date is NOT CORRECT"
else:
    print "Date is CORRECT!"

