num = raw_input("input number: ")

n = 0
res = 0
rg = int(len(num))

while n < rg:
    res = res + (int(num[n])**3)
    n += 1
print "sum cubes of number {} is: {}".format(num, res)
