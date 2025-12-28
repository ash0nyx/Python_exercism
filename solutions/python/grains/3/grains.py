def square(number):
    if number in range(1,65) :
        return 1 << number - 1
    raise ValueError("square must be between 1 and 64")

def total():
    return (1 << 64) - 1
