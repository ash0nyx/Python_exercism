def convert(number):
    drops = ("i",3), ("a",5), ("o",7)
    return "".join(f"Pl{sound}ng" for sound,num in drops if not number % num) or str(number)