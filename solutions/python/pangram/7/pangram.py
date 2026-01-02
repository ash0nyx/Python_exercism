def is_pangram(sentence):
    return set(sentence.lower()) >= set('qwertyuiopasdfghjklzxcvbnm') 