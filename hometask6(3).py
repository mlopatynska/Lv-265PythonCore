def perestanovka(word,*anotherword): 
    for i in range(len(anotherword)): 
        l=0
        if len(word) == len(anotherword[i]): 
            for j in range(len(word)): 
                if not word[j] in anotherword[i]: 
                    break 
                else: 
                     l+=1 
            if l==len(word): 
                print anotherword[i]
              
perestanovka("bara","shabat","raba","shalom","arab")

