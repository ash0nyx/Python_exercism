def convert(number):
    drops = ("i",3), ("a",5), ("o",7)
    return "".join(f"Pl{v}ng" for v,n in drops if not number % n) or str(number)