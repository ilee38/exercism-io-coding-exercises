def sum_of_multiples(limit, multiples):
    if len(multiples) < 1:
        return 0
    mults = set()
    for digit in multiples:
        if digit == 0:
            break
        for i in range(1, limit):
            if digit * i < limit:
                mults.add(digit*i)
            else:
                break
    return sum(mults)
