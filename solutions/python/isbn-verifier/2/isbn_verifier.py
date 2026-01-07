def is_valid(isbn):
    #delete the dashes
    isbn = isbn.replace("-","")
    #check if there are 10 digits
    if len(isbn) != 10 :
        return False

    sum = 0
    #iterate over indexes from 0 to 9
    for index in range(10) :
        char = isbn[index]
        #convert number into integers
        if char.isdecimal() :
            num = int(char)
        #replace X at the end with 10
        elif index == 9 and char == "X" :
            num = 10
        else :
            return False
        #calculate the formula of ISBN
        sum += num * (10 - index)

    #check if the sum is divisble by 11 without a divider
    return sum % 11 == 0