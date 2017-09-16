a = raw_input("Let's make simple addition. Please enter your 'A' value: ")
b = raw_input("Now enter your 'B' value: ")
res_add = int(a) + int(b)
print "The result of %s + %s is %s" % (a, b, res_add)

a = raw_input("Here we will try subtraction. Enter your 'A' value: ")
b = raw_input("Enter your 'B' value: ")
res_sub = int(a) - int(b)
print "The result of %s - %s is %s" % (a, b, res_sub)

a = raw_input("Let's head to multiplication. Enter your 'A' value: ")
b = raw_input("Enter your 'B' value: ")
res_mult = int(a) * int(b)
print "The result of %s * %s is %s" % (a, b, res_mult)

a = raw_input("Division here. Enter your 'A' value: ")
b = raw_input("Enter your 'B' value: ")
res_div = int(a) / int(b)
print "The result of %s / %s is %s" % (a, b, res_div)

a = raw_input("Finally, we can check the remainder of our 2 values. Enter your 'A' value: ")
b = raw_input("Enter your 'B' value: ")
res_mod = int(a) % int(b)
print "The result of %s %% %s is %s" % (a, b, res_mod)