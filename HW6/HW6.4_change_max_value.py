def change_max_items(list1,list2):
    max_list1_index = list1.index(max(list1))
    max_list2_index = list2.index(max(list2))
    list1[max_list1_index], list2[max_list2_index] = list2[max_list2_index], list1[max_list1_index]
    print list1, list2

change_max_items([1,5,67,85,115,45],[1,89,706,54,73,66])