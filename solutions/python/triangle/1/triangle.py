def equilateral(sides):
    (a,b,c) = sides
    if a == b == c and a > 0 :
        return True
    return False


def isosceles(sides):
    (a,b,c) = sides
    if a + b >= c and b + c >= a and a + c >= b and (a == b or b == c or a == c) :
        return True
    return False


def scalene(sides):
    (a,b,c) = sides
    if a + b >= c and b + c >= a and a + c >= b and a!=b and b!=c and a!= c :
        return True
    return False        
