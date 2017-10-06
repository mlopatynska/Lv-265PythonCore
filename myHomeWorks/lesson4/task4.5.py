inputDay = int(raw_input("Write the day you wanna test "))

if (inputDay>365):
    print ("The number you entered is invalid ")
elif (inputDay<1):
    print ("The number you entered is invalid ")
elif ((inputDay%7) == 0):
    inputDay = "sunday"
    print "The day is ",inputDay,"."
elif ((inputDay%6) == 0):
    inputDay = "saturday"
    print "The day is ",inputDay,"."
elif ((inputDay%5) == 0):
    inputDay = "friday"
    print "The day is ",inputDay,"."
elif ((inputDay%4) == 0):
    inputDay = "thursday"
    print "The day is ",inputDay,"."
elif ((inputDay%3) == 0):
    inputDay = "wednesday"
    print "The day is ",inputDay,"."
elif ((inputDay%2) == 0):
    inputDay = "tuesday"
    print "The day is ",inputDay,"."
else:
    inputDay = "monday"
    print "The day is ",inputDay,"."


