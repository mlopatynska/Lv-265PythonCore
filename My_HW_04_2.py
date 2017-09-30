import datetime
import calendar
import time

year = input("Enter year: ")
if datetime.MINYEAR <= year <= datetime.MAXYEAR:
    month = input("Enter month: ")
    if 1 <= month <= 12:
        day = input("Enter day: ")
        if 1 <= day <= calendar.monthrange(year, month):
            if month < 10:
                month = "0" + str(month)
            else:
                month = month
            # print "You entered this date {}/{}/{}".format(year, month, day)
            entered_date = str(year) + "/" + str(month) + "/" + str(day)
            now_date = time.strftime("%Y/%m/%d")
            if entered_date == now_date:
                print "You entered present date. Congratulation!"
            else:
                print "You entered this date: {}/{}/{} but today is: {}".format(year, month, day, now_date)

    else:
        print "Your entered is not correct month!"
else:
    print "Your entered is not correct year!"
