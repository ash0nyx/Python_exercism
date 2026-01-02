def is_pangram(sentence):
    return set('qwertyuiopasdfghjklzxcvbnm') <= set(sentence.lower())