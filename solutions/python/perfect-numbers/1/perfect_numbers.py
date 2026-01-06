def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    #only for positive integers
    if not isinstance(number, int) or number < 1 :
        raise ValueError("Classification is only possible for positive integers.")

    #aliquot sum (sum of divisors without the number itself)
    aliquout = 0
    for num in range (1, number) :
        if number % num == 0 :
            aliquout += num

    #classify if it's perfect, abundant or deficient
    if aliquout == number :
        return "perfect"
    elif aliquout > number :
        return "abundant"
    else:
        return "deficient"