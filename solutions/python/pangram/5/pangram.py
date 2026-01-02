def is_pangram(sentence):
    return set('qwertyuiopasdfghjklzxcvbnm').issubset(sentence.lower())