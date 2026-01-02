def is_pangram(sentence):
    alph = 'qwertyuiopasdfghjklmzxcvbn'
    sentence = sentence.lower()
    for letter in alph :
        if letter not in sentence :
            return False
    return True