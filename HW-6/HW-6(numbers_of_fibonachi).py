num = int(raw_input("input numbers: "))

def fibo(num):
    a, b = 0, 1
    for i in range(2, num + 1):
        print a
        a, b = b, a + b
fibo(num)
