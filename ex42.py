a0 = raw_input("Enter 4-digit number: ")
a = int (a0)
a1 = a % 10
a2 = (a / 10) % 10
a3 = (a / 100) % 10
a4 = (a / 1000) % 10
dob = a1 * a2 * a3 * a4
print "Dobutok cyfr = {}".format(dob)
x = a1*1000 + a2*100 + a3*10 + a4
print "Chyslo u zvorotnyomu poryadky: {}".format(x)
y = sorted(str(a))
print "Posortovani cyfry: {}".format(y)