def fib(n):

n = int(raw_input("Enter N:"))

a1=1
a2=1
for i in range(n):
print ("{}: {}").format(i, a1)
a1,a2 = a2,a1+a2
fib(100)

