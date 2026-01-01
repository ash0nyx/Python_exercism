def score(x, y):
    radius = x**2 + y**2
    x = abs(x)
    y = abs(y)
    if x > 10 or y > 10 or radius > 100 :
        return 0
    elif x > 5 or y > 5 or radius > 25 :
        return 1
    elif x > 1 or y > 1 or radius > 1 :
        return 5
    elif x >= 0 or y >= 0 :
        return 10 
    return "Don't know"