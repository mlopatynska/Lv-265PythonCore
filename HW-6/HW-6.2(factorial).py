n = float(raw_input("input number n: "))
m = float(raw_input("input number m: "))

def calc_factorial(x):
    if x == 0:
        return 1
    return (x * calc_factorial(x - 1))

def fun(n, m):
    n1 = calc_factorial(n)
    m1 = calc_factorial(m)
    nm = calc_factorial(n + m)
    res = n1 * m1 / nm
    return res

print fun(n, m)
