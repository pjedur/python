def birthdays(s):
    x = s.split()
    d = {}
    li = []
    t = ()
    for i in x:
        d.setdefault(i[0:4], []).append(i)
    for j in d:
        if len(d[j]) > 1:
            t = tuple(d[j])
            li.append(t)
    return li

    
