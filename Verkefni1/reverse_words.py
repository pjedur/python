def reverse_words(s):
    x = s.split(" ")
    l = ""
    while x:
        l = l + x.pop() + " "
    return l[:-1]
