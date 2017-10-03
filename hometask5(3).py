F1=1
F2=1
n=input("The meaning of a number N is ")
n=int(n) 
i=2 
while i<n:
    Fibsum=F2+F1
    F1 = F2
    F2 = Fibsum
    i += 1
print ("The Fibonacci sum is %d" %Fibsum)
