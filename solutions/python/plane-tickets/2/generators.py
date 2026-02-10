"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    letters = "ABCD"

    for num in range(number):
        yield letters[num % 4]
    


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    row = 1
    seat = 0

    while seat < number :
        if row == 13 :
            row += 1
            continue

        letters = generate_seat_letters(4)

        for _ in range(4) :
            if seat >= number :
                break
            letter = next(letters)
            yield f"{row}{letter}"
            seat += 1

        row +=1
        

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    assigned_seats = {}
    seats = generate_seats(len(passengers))
    
    for passenger in passengers :
        assigned_seats[passenger] = next(seats)

    return assigned_seats

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for seat_number in seat_numbers :
        #combine seat number and flight ID and left allign the string using '0' to fill the rest
        code = f'{seat_number}{flight_id}'.ljust(12,'0')
        yield code
