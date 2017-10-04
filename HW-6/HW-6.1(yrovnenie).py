a = raw_input("input numberS a: ")
# b = float(raw_input("input number b: "))
# c = float(raw_input("input number c: "))
x = float(raw_input("input number x: "))
# y = float(raw_input("input number y: "))
# z = float(raw_input("input number z: "))
st = []
for el in range(1, 31):
    st.append(el)

# print st
"""proverka st spiska 1 - 30"""

def ymnoz(a, st, x):
    """function dla rjada a1*x^30 + a2*x^29"""
    n = 0
    res = 0
    while n <= 30:
        r_st = st[::-1]
        pw = int(r_st[n])
        res = res + (int(a[n]) * (x ** pw))
        n += 1
        return res
print ymnoz(a, st, x)


