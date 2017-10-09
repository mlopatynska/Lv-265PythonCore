# Hello. This code is not finish because I can not understand how to replace received result according to the task.

import random

a = [[random.randint(1, 800) for el_1a in range(5)] for el_2a in range(5)]
b = [[random.randint(1, 100) for el_1b in range(5)] for el_2b in range(5)]


def martix(lis1):
    m = lis1[0][0]
    pos1 = 0
    pos2 = 0
    for i in range(len(lis1) - 1):
        for j in range(len(lis1[i]) - 1):
            if lis1[i][j] > m:
                pos1 = i
                pos2 = j
                m = lis1[i][j]
    return m, pos1, pos2, lis1


symb1, pos1_lis1, pos2_lis1, list1 = martix(a)
symb2, pos1_lis2, pos2_lis2, list2 = martix(b)
print "We find max symbol {} on position in list A [{}][{}] and the list is: \n {}.".format(symb1, pos1_lis1, pos2_lis1,
                                                                                            list1)
print "We find max symbol {} on position in list B [{}][{}] and the list is: \n {}.".format(symb2, pos1_lis2, pos2_lis2,
                                                                                            list2)
