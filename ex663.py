x = float(raw_input("Enter x:"))

y = (x*(3-x))/(1-x)**3
print ("y= {}").format(y)

n = 1
s = 0
krok = n*(n+2)*x**n
while krok>(10**(-5)):
s = s + krok
n += 1
krok = n*(n+2)*x**n

else:
print ("S= {}").format(s)

Pohybka = abs((s-y)/y)*100
print ("Pohybka= {}").format(Pohybka)


