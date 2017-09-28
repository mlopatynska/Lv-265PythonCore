testedYear = raw_input("Enter the year you wanna test ")
testedYear = int(testedYear)
leapYear = testedYear % 4
if (leapYear == 0):
    print ("This is a leap year")
else:
    print ("This is not a leap year")
