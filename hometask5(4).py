n=input("Number:")
last=0
sum=0
while n>0 :
    last=n%10
    n=n/10
    sum=sum+last**3
    print last
print sum
