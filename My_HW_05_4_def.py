fig = raw_input("Enter natural number: ")


def natural_number(f):
    res = 0
    for element in f:
        res = res + int(element) ** 3
    return "The sum of the cubes of a given natural number is: {}".format(res)


exit = natural_number(fig)
print exit
