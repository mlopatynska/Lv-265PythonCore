def permutations(word,*word1):
    for j in range(len(word1)):
        b=0
        if len(word) == len(word1[j]):
            for i in range(len(word)):
                if not word[i] in word1[j]:
                    #word1[j] = word1[j].replace(word[i], "", 1)
                    break
                else:
                     b +=1
            if b == len(word):
                print word1[j]
permutations("abc","cbacfcrfv", "nfa", "cba", "tyuio", "aaa", "bbb","bac")
