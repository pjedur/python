#!/bin/python
import re
from bs4 import BeautifulSoup as soup
import requests as r
import time
url = 'http://www.imdb.com/chart/top'

def imdb():
    quant = int(input("Type the number of actors you want to see. This list will represent the people who appear most in the top 250 rated films on www.imdb.com: "))
    res = r.get(url)
    s = soup(res.text)
    x = []
    l = []
    for i in s.findAll('a'):
        x.append(i.get('href'))
    for i in x:
        if i.startswith("/title"):
            l.append('http://imdb.com' + i)
    l = list(set(l))
    d= {}
    for k in l:
        res = r.get(k)
        s = soup(res.text)
        for i in s.findAll('a'):
            if i.text == "See full cast":
                a = k.split("?")
                a = a[0]
                a += i.get('href')
                res = r.get(a)
                s = soup(res.text)
                for j in s.findAll('span', {'class':'itemprop'}):
                    q = s.title.text.split("-")
                    q = q[0].strip()
                    if d.get(j.text):
                        d[j.text].append(q)
                    else:
                        d.setdefault(j.text, []).append(q)
    sort = sorted(d, key = lambda x: len(d.get(x)), reverse=True)
    c=1
    for i in sort:
        if quant ==0:
            break
        quant-=1
        print(c, "-", i, ":" , len(d[i]), 'appearances on the list')
        print("Movies =" , d[i])
        c+=1
    
