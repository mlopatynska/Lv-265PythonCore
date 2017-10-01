a = int(raw_input("Enter A:"))

for k in range(1000, 9999):
if (k//1000 + (k%1000)//100 + (k%100)//10 + k%10)==a:
print k