def reverse(text):
    rev = ''

    for letter in text :
        #add current character in front of reversed string
        rev = letter + rev

    return rev