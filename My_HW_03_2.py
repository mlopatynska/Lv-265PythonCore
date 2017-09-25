a = input("Enter natural number with 4 digit only with figures(1,2,3,4,5,6,7,8,9): ")
dil = 10
a1 = a % dil
a2 = (a / dil) % dil
a3 = (a / dil ** 2) % dil
a4 = (a / dil ** 3) % dil
rez_nat = a1 * a2 * a3 * a4
print "Product of natural number = {}".format(rez_nat)
rez_nat = str(a)
rev_nat = rez_nat[::-1]
print "Your reverse natural number is: {}".format(rev_nat)
sor_nat = sorted(rez_nat)
sor_rez_nat = ''.join(sor_nat)
print "Our sorted figure: {}\n\n".format(sor_rez_nat)
