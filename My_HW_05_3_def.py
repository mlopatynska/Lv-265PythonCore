figure = input("Enter number: ")


def fibonacci(num):
    i = 0
    f1 = 0
    f2 = 1
    while i < num:
        f = f1 + f2
        f1 = f2
        f2 = f
        i += 1
        print "Number -{}- of fibonacci is: {} ".format(i, f2)


fibonacci(figure)
