print"Hello! I can help you to recognize leap and not lep year."
year = int(input("Enter year in format XXXX: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print "{} -- It is a leap year!".format(year)
else:
    print "{} -- This is not a leap year!".format(year)
