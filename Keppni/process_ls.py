def process_ls(s):
    s = s.splitlines()
    s = [lambda x: x.split(), s]
    x = [i for i in s if i.startswith("-r")]
    x = list(map(lambda x: x[-1], sorted(s[4])))
    return x

