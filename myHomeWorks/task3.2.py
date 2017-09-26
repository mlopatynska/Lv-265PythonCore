n = input("Enter a four digit number ")
n = int(n)

lastDigit = 0
sum = 0

lastDigit = n%10
n = n/10 
sum = sum+lastDigit
    
print (sum)
