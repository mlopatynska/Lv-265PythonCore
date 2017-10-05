num = raw_input("input number: ")

def stepen(num):
    n = 0
    res = 0
    rg = int(len(num))
    while n < rg:
        res = res + (int(num[n])**3)
        n += 1
        return("sum cubes of number {} is: {}".format(num, res))

print stepen(num)
