text = raw_input("Enter text please: ")
spec_symbol = raw_input("Enter special symbol: ")


def spec_sym(tx, ss):
    spl = tx.split(' ')
    for elem in spl:
        str1 = str(elem)
        if str1.startswith(ss):
            print str1


spec_sym(text, spec_symbol)
