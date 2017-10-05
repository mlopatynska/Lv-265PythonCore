def factorial(num):
    if num == 1:
        return 1
    return factorial(num-1)*num

m = int(raw_input("Enter number m : "))
n = int(raw_input("Enter number n : "))

print factorial(n)*factorial(m)/factorial(n+m)
