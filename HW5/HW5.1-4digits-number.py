mySum = int(input("Enter number "))
for i in range(1000,10000):
    sum = 0
    number = i
    while number:
        lastDigit = number % 10
        number = number / 10
        sum = sum + lastDigit
    if sum == mySum:
        print "Sum {} is in number: {}".format(mySum,i)