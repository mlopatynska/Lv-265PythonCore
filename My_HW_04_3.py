from math import pow, sqrt

print "Enter three valid numbers below."
a = float(input("Enter number a: "))
b = float(input("Enter number b: "))
c = float(input("Enter number c: "))
d = pow(b, 2) - 4 * a * c
if d > 0:
    x1 = (- b + sqrt(d)) / 2 * a
    x2 = (- b - sqrt(d)) / 2 * a
    print "Discriminator > 0. Well, we received two real roots: \nx1 = {} \nand \nx2 = {}".format(x1, x2)
elif d == 0:
    x = -(b / 2 * a)
    print "Discriminator = 0. Well, we received one real roots: x = {}".format(x)
else:
    print "Discriminator < 0. Well, there no real roots."
