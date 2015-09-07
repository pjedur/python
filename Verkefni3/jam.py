def jam(s):
    s = s.replace(", ", ",").replace(" ,", ",").replace(" with ", " and ").replace("plus", "")
    s = s.splitlines()
    d = {}
    for i in s:
        i = i.split(",")
        i = i[1:-1]
        for l in range(len(i)):
            l = i[l].split(" and ")
            for q in l:
                if not q == "":
                    if d.get(q.lstrip()):
                        d[q.lstrip()] += 1
                    else:
                        d.setdefault(q.lstrip(), 1)
    return d


  
