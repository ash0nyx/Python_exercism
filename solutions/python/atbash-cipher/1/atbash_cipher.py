from string import ascii_lowercase

ALPHABET = ascii_lowercase
TRANSLATION = str.maketrans(ALPHABET, ALPHABET[::-1])

def encode(plain_text):
    cleaned = ''.join(character.lower() for character in plain_text if character.isalnum())
    return ' '.join(cleaned.translate(TRANSLATION)[index:index+5] for index in range(0, len(cleaned), 5))

def decode(ciphered_text):
    cleaned = ''.join(character.lower() for character in ciphered_text if character.isalnum())
    return cleaned.translate(TRANSLATION)