def is_valid(isbn):
    #delete the dashes
    isbn = list(isbn.replace("-",""))
    #check if there are 10 digits
    if len(isbn) != 10 :
        return False
    #replace X at the end with 10
    if isbn[-1] == "X" :
        isbn[-1] = "10"
    #check if isbn has only numbers
    if not all([num.isdigit() for num in isbn]) :
        return False
    #check if the sum is divisble by 11 without a divider
    return sum(int(digit) * index for digit, index in zip(isbn, range(10, 0, -1))) % 11 == 0