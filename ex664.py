x = float(raw_input("Enter x:"))

y = (1+x)**(-5/2)
print ("y= {}").format(y)

k = 1
s = 0
krok = 1
while krok>(10**(-5)):
s = s + krok
k += 1
krok = krok*(-((2*k+1)/(2*(k-1)))*x)

else:
print ("S= {}").format(s)

Pohybka = abs((s-y)/y)*100
print ("Pohybka= {}").format(Pohybka)


