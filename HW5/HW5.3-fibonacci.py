myNumber = int(raw_input("Enter a number: "))
i=0
a1=0
a2=1
while i < myNumber:
    num = a1 + a2
    a1 = a2
    a2 = num
    i += 1
    print num