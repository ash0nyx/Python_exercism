def translate(text):
    vowels = "aeiou"
    vowels_y = "aeiouy"
    specials = ["xr", "yt"]
    words = text.split()
    pig = []
    
    for word in words:
        if word[0] in vowels or word[0:2] in specials :
            pig.append(word + "ay")
            continue
            
        for position in range(1, len(word)) :
            if word[position] in vowels_y:
                position += 1 if word[position] == "u" and word[position - 1] == "q" else 0
                pig.append(word[position:] + word[:position] + "ay")
                break
             
    return " ".join(pig)