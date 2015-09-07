def palindrome(n,b):
    if n < b:
        x = format(n)
        return x == x[::-1]
    if b == 10:
        x = format(n)
        return x == x[::-1]
    if b == 2:
        X = bin(n)[2:]
        return X == X[::-1]
    return False
            
    
