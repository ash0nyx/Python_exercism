def check(sides) :
    a,b,c = sorted(sides)
    return a + b >= c and a != 0

def equilateral(sides):
    a,b,c = sorted(sides)
    return check(sides) and a == b == c


def isosceles(sides):
    a,b,c = sorted(sides)
    return check(sides) and a == b or b == c or a == c


def scalene(sides):
    a,b,c = sorted(sides)
    return check(sides) and a!=b and b!=c and a!= c     
