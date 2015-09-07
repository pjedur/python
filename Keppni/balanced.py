def balanced(s):
    if len(s) == 1:
        return False
    x =[]
    for i in s:
        if i is "(":
            x.append(i)
        elif i is ")":
            if not x:
                return False
            else:
                x.pop()
    return True
