fig = raw_input("Enter natural number: ")
res = 0
for element in fig:
    res = res + int(element) ** 3
print "The sum of the cubes of a given natural number is: {}".format(res)
