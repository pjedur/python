def excel_index(s):
    t = 0
    l = (len(s)-1)
    for i in s:
        t += (ord(i)-64) * (26**l)
        l-= 1
    return t
        
        
