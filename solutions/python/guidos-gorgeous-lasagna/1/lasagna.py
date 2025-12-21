"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return  EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers : int - how many layers has the lasagna.
    :return: int - number of layers multiplied by preparation time.
    preparation time is 2 minutes per layer.

    Function that takes the actual number of layers in the lasagna as an argument and 
    returns how many minutes it took to prepare the lasagna based on the 
    `PREPARATION_TIME`.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.

    :param number_of_layers : int - how many layers has the lasagna.
    :elapsed_bake_time : int - how many minutes the lasagne has been in the oven.
    :return: int - number of layers multiplied by preparation time plus elapsed bake 
    time.
    preparation time is 2 minutes per layer.

    Function that takes the preparation time and the elapsed baking time as the 
    arguments and returns how many minutes it took to cook the lasagna sp far.
    """    
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

