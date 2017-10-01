from math import fabs

x = float(raw_input("Enter x:"))

y = 2*x/((1-x)**3)
print ("y= {}").format(y)

k = 1
s = 0
while krok<(10**(-5)):
krok = k*(k+1)*(x**k)
s = s + krok
k += 1

else:
print ("S= {}").format(s)

Pohybka = abs((s-y)/y)*100
print ("Pohybka= {}").format(Pohybka)



