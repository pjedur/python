import re
import urllib
import urllib.request as req
def hungry(a,b,c):
    r = req.urlopen(a)
    q = r.readlines()
    for i in q:
        print(i)
    return q
    
    
