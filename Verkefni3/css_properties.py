import re
def css_properties(s):
    s = s.replace("\n", " ")
    x = re.findall(r"\{(.*?)\}", s)
    l = []
    for i in x:
        i = i.strip().split(";")
        for j in i:
            q = j.split(":")
            if tuple(q) != ('',):
                q[0] = q[0].strip()
                q[1] = q[1].strip()
                l.append(tuple(q))    
    return l
        
