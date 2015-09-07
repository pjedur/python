import re
from bs4 import BeautifulSoup as soup
import requests as r

def imdb():
    res = r.get('http://www.imdb.com/chart/top')
    s = soup(res.text)
    x = []
    for i in s.findAll('a'):
        x.append(i.get('href'))
    l = []
    for i in x:
        if i.startswith("/title"):
            l.append('http://imdb.com' + i)
    l = list(set(l))

    d= {}
    for k in l:
        k = k.split("?")
        k = k[0]
        res = r.get(k)
        s = soup(res.text)
        for j in s.findAll('span', {'class':'itemprop'}):
            q = s.title.text.split("-")
            q = q[0].strip()
            if d.get(j.text):
                d[j.text].append(q)
            else:
                d.setdefault(j.text, []).append(q)

    return d

    #<a href="fullcredits?ref_=tt_cl_sm#cast">See full cast</a>
    '''
    d = {}
    for i in l:
        res = r.get(i)
        s = soup(res.text)
        
        for j in s.findAll('a'):
             if i.text == "See full cast":
                    curr = j.get('href')
                    s = soup(curr.text)
                    
                    for k in s.findAll('span', {'class':'itemprop'}):
                        movie = s.find('a', {'itemprop':"url"})
                        if d[k.text]:
                            d[k.text].append(movie)
                        else:
                            d.setdefault(k.text,[]).append(movie)'''

