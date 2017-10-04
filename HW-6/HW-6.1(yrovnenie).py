a = raw_input("input numberS a: ")
b = raw_input("input numberS b: ")
c = raw_input("input numberS c: ")
x = float(raw_input("input number x: "))
y = float(raw_input("input number y: "))
z = float(raw_input("input number z: "))

st = []
for el in range(1, 21):
    st.append(el)
# print st
"""proverka st spiska 1 - 30"""

def ymnoz_a_b(st, a, x):
    """function dla rjada a1*x^30 + a2*x^29 +  .."""
    n = 0
    res = 0
    while n <= 20:
        r_st = st[::-1] # mozna vynesty na globalny zminu
        pw = int(r_st[n])
        res = res + (int(a[n]) * (x ** pw))
        n += 1
        return res
# print ymnoz_a_b(st, a, x)
"""proverka raboty function (ymnoz_a_b)"""

def znamenyk(st, c, x, z):
    n = 0
    res = 0
    while n <= 20:
        r_st = st[::-1] # mozna vynesty na globalny zminu
        pw = int(r_st[n])
        res = res + (int(c[n]) * ((x + z)**pw))
        n +=1
        return res
# print znamenyk(st, c, x, z)
"""proverka raboty function (znamenyk)"""

global_res = (((ymnoz_a_b(st, a, x)) ** 2) - ((ymnoz_a_b(st, b, y))) / (znamenyk(st, c, x, z)))

print global_res