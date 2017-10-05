def my_sort(list):
    for j in range(len(list)):
        for i in range(len(list)-1-j):
            if list[i]<list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
    return list
print my_sort([2,5,3,100])
print my_sort([6,56,64,43,78])
