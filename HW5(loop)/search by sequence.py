userText = raw_input("Please enter your text: ")
userSeq = raw_input("Please enter sequence you want to find: ")

userText = userText.split()
for word in (userText):
    if userSeq in word:
        print (word),
    else:
        print "No words corresponding to your search input."
        break
