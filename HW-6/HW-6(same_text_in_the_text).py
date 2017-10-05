text = raw_input("input you text: ")
sq = raw_input("input symbols for search: ")

s1 = text.split()

def znaidy(s1, sq):
    for fd in s1:
        if fd.startswith(sq):
            print fd

znaidy(s1, sq)
