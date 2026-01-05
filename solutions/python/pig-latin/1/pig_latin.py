def translate(text):
    vowels = "aeiou"
    words = text.split()
    pig = []
    for word in words:
        # rule 1: vowels, xr, yt
        if word[0] in vowels or word[:2] in ["xr", "yt"] :
            pig.append(word + "ay")
        #rule 4: y
        elif word[0] == "y" :
            pig.append(word[1:] + "yay")
        else :
            for i, letter in enumerate(word) :
                #rule 3: qu
                if letter == "q" and word[i+1] == "u" :
                    pig.append(word[i+2:] + word[:i] + "quay")
                    break
                #rule 2: consonant or y
                elif letter in vowels or letter == "y" :
                    pig.append(word[i:] + word[:i] + "ay")
                    break       
    return " ".join(pig)

