num = raw_input("input numbers: ")
action = raw_input("input 'y' if you need cycle 'for': ")

n = 0
res1 = 0
i = 0
res2 = 0
rg = int(len(num))

def fr_lis(rg, res1, num):
    for n in range(rg):
        res = int(num[n])
        res1 = res1 + res
    return res1

def wh_lis(n, rg, num, res1):
    while n < rg:
        res = int(num[n])
        res1 = res1 + res
        n += 1
    return res1

def fr_num(num, res2):
    for i in range(len(num)):
        num = int(num)
        res_num = num % 10
        num = num / 10
        i += 1
        res2 = res2 + res_num
    return res2

def wh_num(i, rg, num, res2):
    while i < rg:
        num = int(num)
        res_num = num % 10
        num = num / 10
        i += 1
        res2 = res2 + res_num
    return res2

if action == 'y':
    print "you used cycle 'for'"
    print "answer is: {}, calculation with list operations".format(fr_lis(rg, res1, num))
    print "answer is: {}, calculation with numbers operations".format(fr_num(num, res2))

else:
    print "you used cycle 'while'"
    print "answer is: {}, calculation with list operations".format(wh_lis(n, rg, num, res1))
    print "answer is: {}, calculation with numbers operations".format(wh_num(i, rg, num, res2))
