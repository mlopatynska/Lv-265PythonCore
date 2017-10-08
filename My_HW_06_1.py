a = list(range(0, 31))
b = list(range(0, 31))
c = list(range(0, 31))
x = input("Enter number x: ")
y = input("Enter number y: ")
z = input("Enter number z: ")


def velychyna1(x1, a1=a):
    m = 0
    n = len(a1)
    r2 = 0
    while len(a1) > m:
        if n != 0:
            r1 = (a1[m] * x1 ** n)
            n = n - 1
            m = m + 1
            r2 = r2 + r1
        else:
            r2 = r2 + a1[m]
    res1 = r2 ** 2
    return res1


velychyna1(x)


def velychyna2(y1, b1=b):
    m = 0
    n = len(b1)
    r2 = 0
    while len(b1) > m:
        if n != 0:
            r1 = (b1[m] * y1 ** n)
            n = n - 1
            m = m + 1
            r2 = r2 + r1
        else:
            r2 = r2 + b1[m]
    res2 = r2
    return res2


velychyna2(y)


def velychyna3(x1, z1, c1=c):
    m = 0
    n = len(c1)
    r2 = 0
    while len(c1) > m:
        if n != 0:
            r1 = c1[m] * (x1 + z1) ** n
            n = n - 1
            m = m + 1
            r2 = r2 + r1
        else:
            r2 = r2 + c1[m]
    res3 = r2
    return res3


velychyna3(x, z)


def resume(zet1, zet2, zet3):
    return (zet1 - zet2) / zet3


print resume(velychyna1(x), velychyna2(y), velychyna3(x, z))
