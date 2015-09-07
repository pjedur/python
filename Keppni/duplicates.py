def duplicates(s):
    l=[]
    q=[]
    for i in s:
        if i in l:
            q.append(i)
        l.append(i)
    return set(q)
