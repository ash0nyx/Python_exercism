def is_isogram(string):
    #lowercase and only letters from the alphabet (so no symbols)
    cleaned = "".join(letter for letter in string.lower() if letter.isalpha())
    #checking if there are duplicates (cause sets have only unique values)
    return len(cleaned) == len(set(cleaned))