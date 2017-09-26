
a = 3897
print "Our initial number is {}".format(a)

# Sorting numbers first, to convert them to a list
num = str(a)
num_lst = sorted(num)
print "Sorted numbers are: {}".format(num_lst)

# Multiplication of numbers using map & lambda functions

int_lst = map(int, num_lst)
num_mult = reduce((lambda x, y: x*y), int_lst)
print "The result of multiplication of each 'li' element is: {}".format(num_mult)

# Reversing numbers in the initial list

num_rev = num[::-1]
print "The result of reversing initial number is: {}".format(num_rev)
