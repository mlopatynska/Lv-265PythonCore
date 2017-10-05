num = input("Enter number: ")


def prime_number(number):
    if number > 1:
        for elem in range(2, number):
            if number % elem == 0:
                return "This is a not prime number"
        else:
            return "This is a prime number."
    else:
        return "Enter only number more than 1!"


res = prime_number(num)
print res
