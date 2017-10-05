m = int(raw_input("Enter m: "))
n = int(raw_input("Enter n: "))

def my_factorial(k):
    if k == 0:
        return 1
    return (k * my_factorial(k - 1))

    res = my_factorial(n)*my_factorial(m)/my_factorial(n+m)
    
print res

