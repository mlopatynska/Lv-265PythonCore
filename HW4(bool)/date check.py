import datetime
import calendar

print "Note: The date format is yy/mm/dd"
userYear = input("Please enter today's year: ")
inputMonth = raw_input("Please enter today's month: ")

''' str input is better for the date because some people type in month's with leading zeros
which is not allowed as int by Python, thus it is better to take str input and transform it to int '''

userMonth = int(inputMonth)
userDay = input("Please enter today's day: ")

# Converting date string to date obj format

dateStr = ("{}-{}-{}").format(userYear, userMonth, userDay)
dateNow = datetime.datetime.strptime(dateStr, "%Y-%m-%d").date()

nowMonth = calendar.monthrange(userYear, userMonth)

if (1900 <= userYear <= 2120) and (0 <= userMonth <= 12) and (1 <= userDay < nowMonth):
    if datetime.datetime.today().date() == dateNow:
        print "Your date {} is today's date".format(dateNow)
    else:
        print "Your date {} is not today's date".format(dateNow)
else:
    print "Your date format is not valid. Try again"
    
