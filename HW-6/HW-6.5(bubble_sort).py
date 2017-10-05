a = raw_input("input numbers for sort: ")
a = a.split(' ')
b = raw_input("input numbers for sort: ")
b = b.split(' ')


def mysort(x):
    for el in range(len(x) - 1, 0, -1):
        for i in range(el):
            if x[i] > x[i + 1]:
                sr = x[i]
                x[i] = x[i + 1]
                x[i + 1] = sr

mysort(a)
print a

mysort(b)
print b