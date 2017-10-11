def min_vek(arg):
    pidnos = arg[0][0]
    for el in range(len(arg)):
        for i in range(len(arg[el])):
            if arg[el][i] < pidnos:
                pidnos = arg[el][i]
    return pidnos


def max_vek(arg):
    pidnos = arg[0][0]
    for el in range(len(arg)):
        for i in range(len(arg[el])):
            if arg[el][i] > pidnos:
                pidnos = arg[el][i]
    return pidnos

print min_vek([[4,6,1,5],[9,6,3,5],[9,7,3,5]])
print max_vek([[4,6,1,5],[9,6,3,5],[9,7,3,5]])
