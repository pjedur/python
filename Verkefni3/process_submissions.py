import os
def parse_submissions(s):
    li = []
    for root,dirs,files in os.walk(s):
        for f in files:           
            if f == 'data.tcl':
                s = (open(os.path.join(root,f), encoding='utf-8').read())
                s = s.splitlines()
                for i in range(len(s)):
                    if "Problem" in s[i]:
                        if "Accepted" in s[i+2]:
                            li.append((s[i-1][17:], s[i][17:], s[i+1][17:]))
    li = sorted(li, key=lambda x: x[0])
    l = []
    for i in range(len(li)):
        l.append((li[i][2].strip("\n"), li[i][1].strip('\n')))    
    return l
