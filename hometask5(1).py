Sum=input('Задане число n:')
for i in range(1000,9999):
    num=i
    sum=0
    while num>0 :
        last=num%10
        num=num/10
        sum=sum+last
    if sum==Sum:
        print ("Нашій сумі відповідають наступні числа:", i)
