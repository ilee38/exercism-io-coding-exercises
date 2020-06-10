from math import ceil

def square_of_sum(number):
    return ((number * (number + 1)) / 2)**2


def sum_of_squares(number):
    return ceil(((number**3)/3) + ((number**2)/2) + (number/6))


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
