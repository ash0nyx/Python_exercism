def is_armstrong_number(number):
    sum = 0
    for num in map(int, str(number)) :
        sum += num**len(str(number))
    return number == sum