def primes(limit):
    if limit < 2:
        return []

    test_list = bytearray([1]*(limit+1))
    length = len(test_list)

    for i in range(2, length):
        for j in range(2, length):
            if i*j < length:
                test_list[i*j] = 0
            else:
                break

    prime_list = [k for k in range(2,length) if test_list[k]]
    return prime_list
