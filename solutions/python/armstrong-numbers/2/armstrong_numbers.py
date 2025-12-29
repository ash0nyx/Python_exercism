def is_armstrong_number(number):
    return number == sum(num ** len(str(number)) for num in map(int, str(number)))