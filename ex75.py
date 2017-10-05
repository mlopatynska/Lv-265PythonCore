def my_bubble(list):
for i in range(len(list)-1):
for j in range(i):
if list[j]<list[j+1]:
list[j],list[j+1] = list[j+1],list[j]
return list
print my_bubble([3, 1000, 53, 499, 300, 2, 7])