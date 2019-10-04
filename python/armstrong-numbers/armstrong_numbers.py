def is_armstrong_number(number):
    digits = str(number)
    power = len(digits)
    return number == sum(int(x)**power for x in digits)