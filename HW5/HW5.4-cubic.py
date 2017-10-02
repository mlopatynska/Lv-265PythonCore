myNumber = int(input("Enter number "))
sum = 0
while myNumber:
    lastDigit = myNumber % 10
    cub = lastDigit**3
    myNumber = myNumber / 10
    sum = sum + cub
print sum