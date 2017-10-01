text = raw_input("Enter text:")
seq = raw_input("Enter sequence of symbols:")

if len(text)<len(seq):
print ("Sorry, this sequence is longer than entire text :)")

else:
check = True
for i in range(len(seq)):
if text[i]!=seq[i]):
check = False
if check: s = 1
else: s = 0

for j in range(len(text)-len(seq)):
if text[j] = " ":
check = True
for k in range(j+1, j+len(seq)):
if text[k]!=seq[k-j]):
check = False
if check: s += 1


print ("In the text "{}" sequence of symbols "{}" happens {} times).format(text, seq, s)
