import itertools as it
def checklist(s):
    x = True
    for i in range(len(s)-1):
        if s[i]%2 == 0:
            if s[i+1]%2 != 0 or s[i] == s[i+1]:
                continue
            else:
                x = False
        else:
            if ((s[i+1]%2 == 0 and s[i+1] > s[i]) or (s[i+1] < s[i] and s[i+1]%2 != 0)):
                continue
            else:
                x=False
    return x

def numbers_game(s):
    if len(s) < 2:
        s = list(*s)
    for i in s:
        if i > 100 or i < 1:
            return False
        
    s = list(it.permutations(s))
    for i in s:
        if checklist(i) == True:
            return True
    return False
            
            
        
    
