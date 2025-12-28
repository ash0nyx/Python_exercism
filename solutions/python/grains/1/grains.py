def square(number):
    if 1 <= number <= 64 :
        return 2**(number-1)
    raise ValueError("square must be between 1 and 64")

def total():
    number = 1
    total = 0
    while number <= 64 :
        total += (square(number))
        number += 1
    return total
