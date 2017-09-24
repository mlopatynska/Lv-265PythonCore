a = 423106
z = a
b = z % 10
z = z/10
c = z % 10
z = z/10
d = z % 10
z = z/10
e = z % 10
print(a)
print "Product of all numbers", b*c*d*e
print "Reverse", str(a)[::-1]
print sorted(str(a))
