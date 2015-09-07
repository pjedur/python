def process_du(s):
    d = {}
    if len(s) < 2:
        s = list(*s)
    s = s.splitlines()
    for i in s:
        q = i.split(" ")
        q = int(q[0])
        if "/" in i:
            i = i.split("/")
            name = i[-1]
        else:
            i = i.split(" ")
            name = i[-1]
        d[q] = name
    sort = sorted(d, key=lambda x: x, reverse=True)
    l = [d.get(i) for i in sort]
    return l
        
