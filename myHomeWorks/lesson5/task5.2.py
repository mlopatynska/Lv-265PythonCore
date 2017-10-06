num = input('Enter a number ')
start = 2
while num > start :
  if num%start==0 & start!=num:
    print('Your number is not prime.')
    break
  start += 1
else:
   print('Your number is prime.')
