def steps(number):
    #accept only positive integers
    if number < 1 or not isinstance(number, int) :
        raise ValueError("Only positive integers are allowed")

    steps = 0
    while number != 1 :
        #even
        if number % 2 == 0 :
            number /= 2
        #odd
        else :
            number = number * 3 + 1
        steps += 1
    return steps