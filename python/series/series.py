
def slices(series, length):
    """ param series = string sequence of numbers
        param length = length of slices to return
    """
    if length > len(series) or length <= 0:
        raise ValueError("Invalid parameter: length")

    sequences = []
    i = 0
    while True:
        if i + length <= len(series):
            sequences.append(series[i:i+length])
            i += 1
        else:
            break
    return sequences
