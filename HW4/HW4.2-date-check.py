import time
import calendar
y = int(raw_input("Please, enter the year(ex: yyyy):"))
if 3000 > y and y > 0:
    m = int(raw_input("Please, enter the month(ex: mm):"))
else:
    print "Error"
if m>0 and m<13:
    d = int(raw_input("Please, enter the date (ex: dd): "))
else:
    print "Error"
if d >0 and d < calendar.monthrange(y, m)[1]:
    print "OK"
else:
    print "Error"
todayDate = time.strftime("%#d/%#m/%Y")
enterDay = "%s/%d/%s" %(d,m,y)
if enterDay == todayDate:
    print "You entered today's data"
else:
    print "You entered wrong data"
