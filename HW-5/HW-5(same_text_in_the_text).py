text = raw_input("input you text: ")
sq = raw_input("input symbols for search: ")

s1 = text.split()

for fd in s1:
    if fd.startswith(sq):
        print fd
