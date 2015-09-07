def process_ls(s):
    x = s.splitlines()
    l = []
    for i in range(len(x)):
        if x[i].startswith("-r"):
            w = x[i].split()
            r = ",".join(w[8:]).replace(","," ")
            t = (int(w[4]), r)
            l.append(t)
    l = sorted(l, key=lambda x: (x[0],(x[1])), reverse=True)
    "l = l[::-1]"
    return [l[i][1] for i in range(len(l))]
    "return [l[i][1] for i in range(len(l))]"
    '''
    x = [ i.split() for i in s.splitlines()]
    l = []
    for i in x:
        if i[0].startswith("-r"):
            t = (i[4],list(str(i[8::])))
            l.append(t)
    l = sorted(l, key=lambda x: int(x[0]))
    l = l[::-1]
    return [l[i][1] for i in range(len(l))]
           
    l = sorted(l, key=lambda x: int(x[0]))
    l = l[::-1]
    return [l[i][1] for i in range(len(l))]'''
    
    
            
