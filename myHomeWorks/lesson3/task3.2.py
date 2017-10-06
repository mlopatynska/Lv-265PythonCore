n = input("Enter a four digit number ")
n = int(n)

lastDigit = 0
sum = 0

while n:
    lastDigit = n%10
    n = n/10
    sum = sum+lastDigit
    print "lastDigit={}, n = {}, sum = {}".format(lastDigit, n, sum)

print (sum)


