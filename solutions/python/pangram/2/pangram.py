def is_pangram(sentence):
    alph = 'qwertyuiopasdfghjklmzxcvbn'
    for letter in alph :
        if letter not in sentence.lower() :
            return False
    return True