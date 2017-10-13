import random
massiv1=[random.randint(0,100) for i in range(10)]
massiv2=[random.randint(0,100) for i in range(10)]
print massiv1
print massiv2
def mysort(list):
    for j in range(len(list)):
         for i in range(len(list)-1-j): 
              if list[i]<list[i+1]: 
                list[i],list[i+1] = list[i+1],list[i] 

    return list 
mysort(massiv1)
mysort(massiv2)

print mysort(massiv1)
print mysort(massiv2)
