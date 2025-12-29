def response(hey_bob):
    if hey_bob.isspace() or hey_bob == "" :
        return "Fine. Be that way!"
    if hey_bob.isupper() and hey_bob.strip().endswith("?") :
        return "Calm down, I know what I'm doing!"
    if hey_bob.strip().endswith("?") :
        return "Sure."
    if hey_bob.isupper() :
        return "Whoa, chill out!"
    return "Whatever."