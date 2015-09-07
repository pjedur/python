import re
def spell_check(a,b):
    var = set()
    l = []
    #b = re.sub('[""'",.;!/%()]', "", b)
    s= open(a, "r")
    for i in s.readlines():
        var.add(i)
    
    b = b.split(" ")
    for i in b:
        if i not in var:
               l.append(i)
    return l
        
