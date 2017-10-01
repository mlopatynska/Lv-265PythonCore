x = float(raw_input("Enter x:"))

y = (1+x)/(1-x)**2
print ("y= {}").format(y)

k = 1
s = 0
krok = (2*k-1)*x**(k-1)
while krok>(10**(-5)):
s = s + krok
k += 1
krok = (2*k-1)*x**(k-1)

else:
print ("S= {}").format(s)

Pohybka = abs((s-y)/y)*100
print ("Pohybka= {}").format(Pohybka)


