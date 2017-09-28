from math import sqrt

a = float(raw_input("Enter a: "))
b = float(raw_input("Enter b: "))
c = float(raw_input("Enter c: "))

d = b**2 - (4 * a * c)

if d > 0:
  x1 = (-b + sqrt(d)) / (2 * a)
  x2 = (-b - sqrt(d)) / (2 * a)
  print "Quadratic equation {}x*x+{}x+{}=0 has 2 real roots: \nx1={}, \nx2={}".format(a, b, c, x1, x2)
elif d == 0:
  x = -b / (2 * a)
  print "Quadratic equation {}x*x+{}x+{}=0 has 1 real root: \nx={}".format(a, b, c, x)
else:
  print "Quadratic equation {}x*x+{}x+{}=0 doesn't have real roots".format(a, b, c)