# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : generators.py
@Project            : 069_Plane_Tickets_Generator
@CreateTime         : 2026/9/27 15:28
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2026/9/27 15:28 
@Version            : 1.0
@Description        : https://exercism.org/tracks/python/exercises/plane-tickets/edit
"""

"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    letters = ['A', 'B', 'C', 'D']
    current_number = 0
    for n in range(number):
        yield letters[current_number]
        current_number = current_number + 1
        if current_number == 4:
            current_number = 0


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    letters = generate_seat_letters(number)
    current_number = 1
    for n in range(1, number + 1):

        letter = next(letters)
        yield str(current_number) + letter

        if n % 4 == 0:
            current_number = current_number + 1
            if current_number == 13: current_number = 14


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seats = generate_seats(len(passengers))
    output = {}
    for passenger in passengers:
        output[passenger] = next(seats)
    return output
    pass


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """
    for seat_number in seat_numbers:
        code = seat_number + flight_id
        yield code + '0' * (12 - len(code))

    pass

# lets_try = generate_seat_letters(9)
# seats = generate_seats(10)
# for x in range(10):
#     # print(next(lets_try))
#     print(next(seats))
#
# print(assign_seats(['aa', 'bb', 'cc', 'dd', 'ee','fff']))
#
# seat_numbers = ['1A', '17D']
# flight_id = 'CO1234'
# ticket_ids = generate_codes(seat_numbers, flight_id)
# print(next(ticket_ids))
# print(next(ticket_ids))
# print(next(ticket_ids))
# print(next(ticket_ids))
