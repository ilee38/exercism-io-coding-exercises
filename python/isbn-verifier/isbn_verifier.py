def is_valid(isbn):
    partial_sum = 0
    position = 10
    if len(isbn) == 10 or len(isbn) == 13:
        for n in isbn:
            if n.isdigit():
                partial_sum += (int(n) * position)
                position -= 1
            elif position == 1 and n == "X":
                partial_sum += 10
        return partial_sum % 11 == 0
    return False
