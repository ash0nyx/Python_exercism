def score(x, y):
    radius = x**2 + y**2
    if abs(x) > 10 or abs(y) > 10 or radius > 100 :
        return 0
    elif abs(x) > 5 or abs(y) > 5 or radius > 25 :
        return 1
    elif abs(x) > 1 or abs(y) > 1 or radius > 1 :
        return 5
    elif abs(x) >= 0 or abs(y) >= 0 :
        return 10 
    return "Don't know"