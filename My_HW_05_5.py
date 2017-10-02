text = raw_input("Enter text please: ")
spec_symbol = raw_input("Enter special symbol: ")
spl = text.split(' ')
for elem in spl:
    str1 = str(elem)
    if str1.startswith(spec_symbol):
        print str1
    else:
        print "We can not find eny words with special symbols."
