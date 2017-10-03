n = input('Enter a number ')

a = 1
b = 2
float(a)
float(b)

while n > 0:
    n -= 1
    F = a + b
    a, b = b, (a + b)
    print F
