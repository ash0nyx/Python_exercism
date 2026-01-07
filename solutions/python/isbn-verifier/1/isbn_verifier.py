def is_valid(isbn):
    isbn = isbn.replace("-","")
    if len(isbn) != 10 :
        return False

    sum = 0
    for index in range(10) :
        char = isbn[index]
        if char.isdecimal() :
            num = int(char)
        elif index == 9 and char == "X" :
            num = 10
        else :
            return False
        sum += num * (10 - index)

    return sum % 11 == 0