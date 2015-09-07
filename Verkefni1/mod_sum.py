def mod_sum(n):
    x = 0
    while n > 0:
        n = n - 1
        if(n % 3 == 0 or n % 5 == 0):
            x += n
    return x
            
