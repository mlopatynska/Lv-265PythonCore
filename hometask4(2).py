import time 
import calendar 
y = int(raw_input("Enter the year:")) 
if y > 0: 
    m = int(raw_input("Enter the month:"))
else: 
     print "It's imposible!" 
if m>0 and m<=12: 
     d = int(raw_input("Enter the date:")) 
else: 
     print "It's imposible!"
if d >0 and d < calendar.monthrange(y, m)[1]: 
     print "Great!" 
else: 
    print "It's imposible!"     
tD = time.strftime("%#d/%#m/%Y") 
eD = "%s/%d/%s" %(d,m,y) 
if eD == tD: 
     print "The data is right)" 
else: 
     print "The data is wrong(" 
