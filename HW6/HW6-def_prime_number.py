def prime(number):
    d = 2
    while (number % d != 0):
        d +=1
    if d == number:
        print "{} is a prime number".format(number)
    else:
        print "{} is NOT a prime number".format(number)
prime(100)
