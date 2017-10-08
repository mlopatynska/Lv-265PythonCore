a = list(input("Enter first massive: "))
b = list(input("Enter second massive: "))


def mysort(x):
    k = 0
    while len(x) - 1 > k:
        for i in range(0, len(x) - 1):
            if (x[i] < x[i + 1]):
                x[i], x[i + 1] = x[i + 1], x[i]
        k += 1
    return x


res1 = mysort(a)
res2 = mysort(b)
print res1
print res2
