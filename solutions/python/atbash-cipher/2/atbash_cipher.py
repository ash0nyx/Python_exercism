from string import ascii_lowercase as asc_low

ENCODING = str.maketrans(asc_low, asc_low[::-1])

def encode(plain_text):
    res = ''.join(chr for chr in plain_text.lower() if chr.isalnum()).translate(ENCODING)
    return ' '.join(res[ind:ind+5] for ind in range(0, len(res), 5))

def decode(ciphered_text):
    return ''.join(chr for chr in ciphered_text if chr.isalnum()).translate(ENCODING)