def filter_sum(s):
    x = [i for i in s if i <= 95 and i >= 10]
    return (sum(x), x)
