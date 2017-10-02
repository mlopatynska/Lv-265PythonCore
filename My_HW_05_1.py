fig_inp = input("Enter num: ")
div = 10
for fig in range(1000, 9999):
    a1 = fig % div
    a2 = (fig / div) % div
    a3 = (fig / div ** 2) % div
    a4 = (fig / div ** 3) % div
    res = a1 + a2 + a3 + a4
    if res == fig_inp:
        print "The sum of this --{}-- digits of a four-digit number is equal to the input.".format(fig)
