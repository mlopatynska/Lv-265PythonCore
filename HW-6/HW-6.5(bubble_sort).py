a = raw_input("input numbers for sort: ")
"""list of elements for sorting"""
a = a.split(' ')
"""make list without space"""
b = raw_input("input numbers for sort: ")
b = b.split(' ')


def mysort(x):
    """create a function"""
    for el in range(len(x) - 1, 0, -1):
        """cycling el in range. Range start: len of list -1, stop: at first element of list, step: revers cycle."""
        for i in range(el):
            """repeat for i(index of list) in range el"""
            if x[i] > x[i + 1]:
                """if x[i] > x[i+1] when do"""
                sr = x[i]
                """write x[i] to sr"""
                x[i] = x[i + 1]
                """replace the x[i] with x[i+1]"""
                x[i + 1] = sr
                """for next time x[i+1] is sr"""

mysort(a)
"""make sorting list a"""
print a
"""print sorted list a"""

mysort(b)
print b
