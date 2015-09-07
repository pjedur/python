import os
import csv
def process_csv(s):
    d = {}
    with open(s, "r") as f:
        r = csv.reader(f, delimiter=',', quotechar='"')
        for i in r:
            x=(int(i.pop()) * int(i.pop()))
            q = ""
            i.pop()
            if i[0] == "mr":
                i[0] = "mr,"
            for j in i:
                q+= j
            if q in d:
                d[q] += x
            else:
                d[q] = x
    return d
            
            
            
            
            
