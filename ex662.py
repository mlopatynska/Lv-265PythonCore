from math import abs, factorial, exp

x = float(raw_input("Enter x:"))

y = (x-1)*exp(x)+1
print ("y= {}").format(y)

k = 1
s = 0
krok = (x**(k+2))/(factorial(k)*(k+2))
while krok>(10**(-5)):
s = s + krok
k += 1
krok = (x**(k+2))/(factorial(k)*(k+2))

else:
print ("S= {}").format(s)

Pohybka = abs((s-y)/y)*100
print ("Pohybka= {}").format(Pohybka)



