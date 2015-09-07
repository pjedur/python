import re
import urllib
import urllib.request as req
import json
def companies(x, y, z):
    z = str(z)
    if x <10:
        x = "4"+str(x)
    else:
        x = str(x)
        c = int(x[0]) + 4
        x = str(c) + x[1]
    if y<10:
        y = "0"+str(y)
        
    l = x+str(y)+z[-2:]
    r = req.urlopen('http://apis.is/company?socialnumber=%s' % l)
    t = json.loads(r.read().decode('UTF-8')) 
    return [t['results'][i]['name'] for i in range(len(t['results'])) if t['results'][i]['active']]
  
  
    
