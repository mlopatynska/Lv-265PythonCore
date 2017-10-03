mySymbols=raw_input("Enter please first symbols: ")
str = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex./n" \
      "Complex is better than complicated. Flat is better than nested. Sparse is better than dense. /n" \
      "Readability counts. Special cases aren't special enough to break the rules."
nStr = str.split(" ")
for i in range(0,len(nStr)):
    if nStr[i].startswith(mySymbols):
          print nStr[i]
