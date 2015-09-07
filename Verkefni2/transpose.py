def transpose(a):
    l = list(zip(*a))
    return [list(l[i]) for i in range(len(l))]
    
