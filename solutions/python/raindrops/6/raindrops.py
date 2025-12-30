def convert(number):
    return "".join(f"Pl{sound}ng" for sound,num in [("i",3), ("a",5), ("o",7)] if not number % num) or str(number)