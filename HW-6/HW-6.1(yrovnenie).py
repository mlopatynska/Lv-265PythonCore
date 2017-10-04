a = raw_input("input numberS a: ")
b = raw_input("input numberS b: ")
c = raw_input("input numberS c: ")
x = float(raw_input("input number x: "))
y = float(raw_input("input number y: "))
z = float(raw_input("input number z: "))

st = []
for el in range(0, 31):
    st.append(el)
r_st = st[::-1]
# print r_st
"""proverka r_st spiska 0 - 30"""

n = 0
res = 0

def ymnoz_a_b(n, res, r_st, a, x):
    """function dla rjada a1*x^30 + a2*x^29 +  .. i dla b y"""
    while n <= 30:
        pw = int(r_st[n])
        res = res + (int(a[n]) * (x ** pw))
        n += 1
        return res
# print ymnoz_a_b(n, res, r_st, a, x)
"""proverka raboty function (ymnoz_a_b)"""

def znamenyk(n, res, r_st, c, x, z):
    while n <= 30:
        pw = int(r_st[n])
        res = res + (int(c[n]) * ((x + z) ** pw))
        n += 1
        return res
# print znamenyk(st, c, x, z)
"""proverka raboty function (znamenyk)"""

global_res = (((ymnoz_a_b(n, res, r_st, a, x)) ** 2) - ((ymnoz_a_b(n, res, r_st, b, y))) / (znamenyk(n, res, r_st, c, x, z)))

print global_res
