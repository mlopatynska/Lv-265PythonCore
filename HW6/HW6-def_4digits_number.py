def four_digit_sum(number):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    if number == i+j+k+l:
                        print "%d%d%d%d"%(i,j,k,l)

four_digit_sum(11)
