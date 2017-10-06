n = input('Enter a number ')
n = int(n)

lastDigit = 0
sum = 0

while n>0:
    lastDigit = n%10
    cub = lastDigit**3
    n = n/10
    sum = sum+cub
    print "lastDigit={}, cub={}, n = {}, sum = {}".format(lastDigit, cub, n, sum)

print sum
