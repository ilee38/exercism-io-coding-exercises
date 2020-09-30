def factors(value):
    if value < 2:
        return []
    prime_factors = []
    while value > 1:
        for div in range(2, value+1):
            if value % div == 0:
                if is_prime(div):
                    prime_factors.append(div)
                    value //= div
                    break
    return prime_factors


def is_prime(n):
    ''' Primality check using the sieve of Erathostenes
    '''
    primes = bytearray([1]*(n+1))
    for i in range(2, n):
        if primes[i]:
            for j in range(i, n):
                if i*j < n:
                    primes[i*j] = 0
                else:
                    break
    return primes[n]
