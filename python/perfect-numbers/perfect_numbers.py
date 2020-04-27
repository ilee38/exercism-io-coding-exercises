
def classify(number):
    if number <= 0:
        raise ValueError("Number must be greater than 0")

    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    if sum == number:
        return "perfect"
    elif sum > number:
        return "abundant"
    else:
        return "deficient"

