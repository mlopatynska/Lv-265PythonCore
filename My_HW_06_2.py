first = input("Enter first number: ")
second = input("Enter second number: ")


def factor(f, s):
    if f <= 1 or s <= 1:
        return 1
    else:
        for i in range(f, s):
            res = f * (i + 1)
            f = res
        return res


finish = factor(first, second)
print finish
