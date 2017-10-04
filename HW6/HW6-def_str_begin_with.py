def words_begin_sequence(text,sq):
    mas = text.split(" ")
    rs = filter(lambda el : el.startswith(sq), mas)
    print rs

words_begin_sequence("Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex./n" \
      "Complex is better than complicated. Flat is better than nested. Sparse is better than dense. /n" \
      "Readability counts. Special cases aren't special enough to break the rules.","b")
